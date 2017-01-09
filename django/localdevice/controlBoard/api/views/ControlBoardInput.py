from threading import Thread

import time
import serial
from django.core.cache import cache
from rest_framework import generics
from rest_framework import mixins

from controlBoard.api.serializers import ControlBoardInSerializer, ControlBoardOutSerializer
from controlBoard.models import ControlBoardInput, ControlBoardOutput

#>>> ser.write(bytes([0x57,0x58,0x0,0x66,0x00,0x0c,0x03,0x01,9,0x2e]))
#>>> ser.write(bytes([87,88,0,102,0,1,3,1,9,35]))
#>>> ser.write(bytes([0x57,0x58,0x0,0x66,0x00,0x01,0x03,0x01,9,0x23]))


frameId = 1

def getFrameId():
    global frameId
    fi = cache.get('frameId')
    if(fi == None):
        cache.set('frameId', frameId)
        fi = frameId
    if(fi>=255):
        fi=1;
    ret = [0x57,0x58,0x00,0x66, 0x00] + [fi] #['%0.2X'%frameId]  '0x{0:02x}'.format
    print(ret)
    cache.set('frameId', fi+1)
    return ret


def turnSlot(opsId, slotNo):
    toBeSumed = getFrameId()+[opsId] + [1] + [slotNo]
    summedUp = sum(toBeSumed) % 256
    lastVal = toBeSumed + [summedUp]
    return lastVal


class ControlBoardInputView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ControlBoardInput.objects.all();
    serializer_class = ControlBoardInSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        slotNo = int(data['slotNo']) if (isinstance(data['slotNo'], str)) else data['slotNo']
        firstCmd = turnSlot(3, slotNo)
        if not request.data._mutable:
            request.data._mutable = True
        data['inputDesc'] = str(firstCmd)
        response = self.create(request, *args, **kwargs)

        print(request.data)
        inputCreated = ControlBoardInput.objects.get(pk=response.data['id'])

        rotateCoil = RotateCoil(data, inputCreated, firstCmd);
        rotateCoil.setDaemon(True);
        rotateCoil.start();

        # rotateRet = rotate(request.data)
        # cboutput = ControlBoardOutput(input=inputCreated, outputDesc=rotateRet)
        # cboutput.save()
        return response

class RotateCoil(Thread):
    def __init__(self, data, inputCreated, firstCmd):
        Thread.__init__(self)
        self.slotNo = int(data['slotNo']) if (isinstance(data['slotNo'], str)) else data['slotNo']
        self.turnCnt = int(data['turnCnt']) if (isinstance(data['turnCnt'], str)) else data['turnCnt']
        self.inputCreated = inputCreated
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        self.firstCmd = firstCmd

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
                    cboutput = ControlBoardOutput(input=self.inputCreated, outputDesc='Error open Ser')
                    cboutput.save()

        tryoutCnt = 1
        result = []
        print("turnCnt: %d" % (self.turnCnt))
        while (ser.is_open == True and tryoutCnt <= self.turnCnt):
            print("tryoutCnt: %d" % (tryoutCnt))
            if(tryoutCnt == 1):
                turnCmd = self.firstCmd;
            else:
                turnCmd = turnSlot(3, self.slotNo)
            ser.flushInput()
            ser.flushOutput()
            ser.write(bytes(turnCmd))
            time.sleep(1)
            out = []
            while ser.in_waiting > 0:
                out += [ser.read(1).hex()]
            print(out)
            result.append(out)
            if (out[6:9] != ['03', '01', '00']):
                #error happened
                print("error while loop turnCnt: " + str(out[6:9]))
                break
            if (tryoutCnt < self.turnCnt):
                time.sleep(2)
            tryoutCnt += 1
        cboutput = ControlBoardOutput(input=self.inputCreated, outputDesc=result)
        cboutput.save()

