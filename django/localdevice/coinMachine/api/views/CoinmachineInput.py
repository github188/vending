from threading import Thread

import time
import serial
from rest_framework import generics
from rest_framework import mixins


#>>> ser.write(bytes([0x05,0x10,0x00,0x10,0x12,0x37]))
from coinMachine.models import CoinMachineInput, CoinMachineOutput
from coinMachine.serializers import CoinMachineInSerializer

prefix = [0x05, 0x10, 0x00, 0x10]

def drive(coinToPay):
    toBeSumed = prefix + [coinToPay]
    summedUp = sum(toBeSumed) % 256
    lastVal = toBeSumed + [summedUp]
    return lastVal


class CoinMachineInputView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CoinMachineInput.objects.all();
    serializer_class = CoinMachineInSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        payoutCnt = int(data['payoutCnt']) if (isinstance(data['payoutCnt'], str)) else data['payoutCnt']
        firstCmd = drive(payoutCnt)
        # if data._mutable and data._mutable is False:
        #     data._mutable = True
        data['inputDesc'] = str(firstCmd)
        response = self.create(request, *args, **kwargs)

        print(request.data)
        inputCreated = CoinMachineInput.objects.get(pk=response.data['id'])

        coinMachineRun = CoinMachineRun(data, inputCreated);
        coinMachineRun.setDaemon(True);
        coinMachineRun.start();

        # rotateRet = rotate(request.data)
        # cboutput = CoinMachineOutput(input=inputCreated, outputDesc=rotateRet)
        # cboutput.save()
        return response

class CoinMachineRun(Thread):
    def __init__(self, data, inputCreated):
        Thread.__init__(self)
        self.payoutCnt = int(data['payoutCnt']) if (isinstance(data['payoutCnt'], str)) else data['payoutCnt']
        self.inputCreated = inputCreated
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

    def run(self):
        ser = self.ser
        tryoutCnt = 1
        while ser.is_open == False and tryoutCnt <= 3:
            time.sleep(2)
            try:
                ser.open()
                tryoutCnt += 1
            except Exception as e:
                print(str(e))
                if(tryoutCnt == 3):
                    cboutput = CoinMachineOutput(input=self.inputCreated, outputDesc='Error open Ser')
                    cboutput.save()

        payoutCmd = drive(self.payoutCnt)
        ser.flushInput()
        ser.flushOutput()
        ser.write(bytes(payoutCmd))
        time.sleep(1)
        out = []
        while ser.in_waiting > 0:
            out += [ser.read(1).hex()]
        print(out)
        cboutput = CoinMachineOutput(input=self.inputCreated, outputDesc=out)
        cboutput.save()

