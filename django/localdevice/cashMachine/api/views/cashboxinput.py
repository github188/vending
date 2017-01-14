from threading import Thread

import time

from pip._vendor import requests
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView

from cashMachine.api.serializers import CashboxOperateSerializer
from cashMachine.libitlsso import LibItlSSO
from cashMachine.models.cashboxlog import CashboxLog
from cashMachine.models.cashboxoperate import CashboxOperate


class CashBoxInputDetailView(RetrieveAPIView):
    queryset = CashboxOperate.objects.all();
    serializer_class = CashboxOperateSerializer
    lookup_field = 'id'

class CashBoxInputView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CashboxOperate.objects.all().order_by("-id")[:50];
    serializer_class = CashboxOperateSerializer
    libItlSSO = LibItlSSO()
    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        response = self.create(request, *args, **kwargs)
        print(response.data['id'])
        inputCreated = CashboxOperate.objects.get(pk=response.data['id'])
        operateCashbox = OperateCashbox(request.data, inputCreated=inputCreated, libItlSSO=self.libItlSSO)
        operateCashbox.setDaemon(True)
        operateCashbox.start()
        return response


class OperateCashbox(Thread):
    def __init__(self, requestData, inputCreated, libItlSSO):
        Thread.__init__(self)
        self.operateName = requestData['operateName']
        tmp = requestData['operateData'];
        self.operateData =  0 if tmp is None or (isinstance(tmp, str) and len(tmp)== 0)  else int(tmp)
        self.libItlSSO = libItlSSO
        self.inputCreated = inputCreated
        # single thread need to be guaranteed. https://docs.python.org/3/library/threading.html

    def run(self):
        if(self.operateName == 'toll'):
            isCharge = self.operateData == 0
            payoutAvailableCnt = self.libItlSSO.payoutCnt()
            if(payoutAvailableCnt<90):
                return -1
            amountToDo = self.operateData
            if(self.libItlSSO.configValidator(amountToDo)<0):
                return -2
            while amountToDo > 0 or isCharge:
                creditNoteValue = self.libItlSSO.creditOne(120)
                # timeout or terminate request happened
                if (creditNoteValue <= 0):
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=creditNoteValue, operateStatus='terminated')
                    cashboxLog.save()
                    return -1;
                else :
                    amountToDo -= creditNoteValue
                    if  amountToDo > 0 :
                        cashboxLog = CashboxLog(operate=self.inputCreated, retData=creditNoteValue, operateStatus='processing')
                    else :
                        cashboxLog = CashboxLog(operate=self.inputCreated, retData=creditNoteValue, operateStatus='succeed')
                    cashboxLog.save()

            if(isCharge):
                return 0;
            payoutCnt = amountToDo // -10
            print("need payoutCnt: %d" % payoutCnt)
            if(payoutCnt > 0):
                time.sleep(3)
            while payoutCnt > 0:
                if self.libItlSSO.payoutNote() == -1 :
                    print("payout failed")
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='failed')
                    cashboxLog.save()
                    break;
                payoutCnt -= 1
                if(payoutCnt > 0):
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='processing')
                else:
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='succeed')
                cashboxLog.save()
            payoutCoinCnt = -amountToDo%10;
            print("payoutCoinCnt: %d" % payoutCoinCnt)
            if(payoutCoinCnt>0):
                response1 = requests.post('http://localhost:8000/api/data/coinmachine/run/', {'payoutCnt': payoutCoinCnt})
                print("coinmachinerun response: "+response1.text)
                # response2 = requests.post('http://172.18.0.4/api/data/coinchangelog/create/', {'amountBefore': -payoutCoinCnt})
                # print("coinmachinerun response: " + response1.content)
            return 0

        if(self.operateName == 'terminate'):
            self.libItlSSO.setRunningStatusToFalse()
            return 0;

        if (self.operateName == 'charge'):
            # only allow 10 to be charged;
            self.libItlSSO.configValidator(-10)
            channelCnt = (300 - self.libItlSSO.payoutCnt())//10
            while(channelCnt > 0 ):
                creditNoteValue = self.libItlSSO.creditOne(120)
                channelCnt -= 1
                if (creditNoteValue <= 0):
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=creditNoteValue, operateStatus='terminated')
                    cashboxLog.save()
                    return 0
                else:
                    if(channelCnt == 1):
                        cashboxLog = CashboxLog(operate=self.inputCreated, retData=0, operateStatus='succeed')
                    else:
                        cashboxLog = CashboxLog(operate=self.inputCreated, retData=creditNoteValue, operateStatus='processing')
                cashboxLog.save()
            return 0;

        if (self.operateName == 'clearPayout'):
            emptyCnt = self.libItlSSO.emptyStore()
            cashboxLog = CashboxLog(operate=self.inputCreated, retData=emptyCnt, operateStatus='succeed')
            cashboxLog.save()

        if (self.operateName == 'payout'):
            amountToDo = self.operateData/10
            while(amountToDo >0):
                if self.libItlSSO.payoutNote() == -1:
                    print("payout failed")
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='failed')
                    cashboxLog.save()
                    break;
                amountToDo -= 1
                if(amountToDo > 0):
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='processing')
                else:
                    cashboxLog = CashboxLog(operate=self.inputCreated, retData=10, operateStatus='succeed')
                cashboxLog.save()


        if (self.operateName == 'currentPayoutAvailable'):
            payoutCnt = self.libItlSSO.payoutCnt()
            cashboxLog = CashboxLog(operate=self.inputCreated, retData = payoutCnt, operateStatus='succeed')
            cashboxLog.save()


        if (self.operateName == 'payoutCoin'):
            amountToDo = self.operateData
            requestData = {'payoutCnt': amountToDo}
            response = requests.post('http://localhost:8000/api/data/coinmachine/run/', requestData)
            print(response)

