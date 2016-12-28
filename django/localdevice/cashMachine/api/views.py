# import math
#
# import time
# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.generics import RetrieveAPIView, ListAPIView
#
# from cashMachine.api.serializers import CashboxOperateSerializer, CashboxLogSerializer
# from cashMachine.libitlsso import LibItlSSO
# from cashMachine.models import CashboxOperate, CashboxLog
#
# class CashBoxLogView(ListAPIView):
#     # queryset1 = CashboxLog.objects.all().order_by("-id")[:10]  #[::-1]
#     queryset = CashboxLog.objects.filter(operate__operateName__exact="toll").order_by("-id")[:10]
#     serializer_class = CashboxLogSerializer
#
# class CashBoxLogByOperateView(ListAPIView):
#     serializer_class = CashboxLogSerializer
#     def get_queryset(self):
#         operate = self.kwargs['operate']
#         return CashboxLog.objects.filter(operate=operate)
#
# class CashBoxLogDetailView(RetrieveAPIView):
#     queryset = CashboxLog.objects.all()
#     serializer_class = CashboxLogSerializer
#     lookup_field = 'id'
#
# class CashBoxInputDetailView(RetrieveAPIView):
#     queryset = CashboxOperate.objects.all();
#     serializer_class = CashboxOperateSerializer
#     lookup_field = 'id'
#
# class CashBoxInputView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = CashboxOperate.objects.all();
#     serializer_class = CashboxOperateSerializer
#     libItlSSO = LibItlSSO()
#     def __init__(self):
#         super().__init__()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         operateCashbox = OperateCashbox(request.data, self.libItlSSO)
#         print(request.data)
#         response = self.create(request, *args, **kwargs)
#         print(response.data['id'])
#         inputCreated = CashboxOperate.objects.get(pk=response.data['id'])
#         operateCashbox.doer(inputCreated)
#         return response
#
#
# class OperateCashbox():
#     def __init__(self, requestData, libItlSSO):
#         self.operateName = requestData['operateName']
#         self.operateData =  0 if len(requestData['operateData']) == 0  else int(requestData['operateData'])
#         self.libItlSSO = libItlSSO
#
#     def doer(self, inputCreated):
#         if(self.operateName == 'toll'):
#             payoutAvailableCnt = self.libItlSSO.payoutCnt()
#             if(payoutAvailableCnt<10):
#                 return -1
#             amountToDo = self.operateData
#             self.libItlSSO.configValidator(amountToDo)
#             while amountToDo > 0:
#                 creditNoteValue = self.libItlSSO.creditOne()
#                 amountToDo -= creditNoteValue
#                 if (creditNoteValue == 0):
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=creditNoteValue, operateStatus='failed')
#                     cashboxLog.save()
#                     break;
#                 if amountToDo> 0:
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=creditNoteValue, operateStatus='processing')
#                 else:
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=creditNoteValue, operateStatus='succeed')
#                 cashboxLog.save()
#             payoutCnt = amountToDo / -10
#             print("need payoutCnt: %d" % payoutCnt)
#             if(payoutCnt > 0):
#                 time.sleep(5)
#             while payoutCnt > 0:
#                 if self.libItlSSO.payoutNote() == -1 :
#                     print("payout failed")
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='failed')
#                     cashboxLog.save()
#                     break;
#                 payoutCnt -= 1
#                 if(payoutCnt > 0):
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='processing')
#                 else:
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='succeed')
#                 cashboxLog.save()
#             return 0
#
#         if (self.operateName == 'charge'):
#             amountToDo = self.operateData
#             if(amountToDo > 0):
#                 amountToDo = - amountToDo
#             if(amountToDo % 5 != 0):
#                 return -1
#             self.libItlSSO.configValidator(amountToDo)
#             channelCnt = self.libItlSSO.channelCnt()
#             while(channelCnt > 0):
#                 creditNoteValue = self.libItlSSO.creditOne()
#                 channelCnt -= 1
#                 if (creditNoteValue == 0):
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=creditNoteValue, operateStatus='failed')
#                     break;
#                 else:
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=creditNoteValue, operateStatus='processing')
#                     cashboxLog.save()
#
#         if (self.operateName == 'clearPayout'):
#             emptyCnt = self.libItlSSO.emptyStore()
#             cashboxLog = CashboxLog(operate=inputCreated, retData=emptyCnt, operateStatus='succeed')
#             cashboxLog.save()
#
#         if (self.operateName == 'payout'):
#             amountToDo = self.operateData/10
#             while(amountToDo >0):
#                 if self.libItlSSO.payoutNote() == -1:
#                     print("payout failed")
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='failed')
#                     cashboxLog.save()
#                     break;
#                 amountToDo -= 1
#                 if(amountToDo > 0):
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='processing')
#                 else:
#                     cashboxLog = CashboxLog(operate=inputCreated, retData=10, operateStatus='succeed')
#                 cashboxLog.save()
#
#
#         if (self.operateName == 'currentPayoutAvailable'):
#             payoutCnt = self.libItlSSO.payoutCnt()
#             cashboxLog = CashboxLog(operate=inputCreated, retData = payoutCnt, operateStatus='succeed')
#             cashboxLog.save()
