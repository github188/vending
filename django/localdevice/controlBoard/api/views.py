import threading
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
    # fmt = '{:02X}' * len(lastVal)
    # lastStr = fmt.format(*lastVal) #str.join("",("%02X" % i for i in lastVal))
    # ret = bytes.fromhex(lastStr)

    return lastVal


class ControlBoardInputView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ControlBoardInput.objects.all();
    serializer_class = ControlBoardInSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        rotateRet = rotate(request.data)
        print(request.data)
        response = self.create(request, *args, **kwargs)
        print(response.data['id'])
        inputCreated = ControlBoardInput.objects.get(pk=response.data['id'])
        cboutput = ControlBoardOutput(input=inputCreated, outputDesc=rotateRet)
        cboutput.save()
        return response

def rotate(data):
    print(data)
    times = int(data['turnCnt']) if(isinstance(data['turnCnt'], str)) else data['turnCnt']
    slotNo = int(data['slotNo']) if(isinstance(data['slotNo'], str)) else data['slotNo']
    inputarr = []
    result = []
    ser = serial.Serial(
        port='/dev/ttyUSB1', baudrate=9600, parity=serial.PARITY_NONE
        , stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
    tryoutCnt = 1
    while ser.is_open==False and tryoutCnt <= 3 :
        time.sleep(2)
        try:
            ser.open()
            tryoutCnt += 1
        except Exception as e:
            print(str(e))
    tryoutCnt = 1
    while(ser.is_open == True and tryoutCnt <= times) :
        ser.flushInput()
        ser.flushOutput()
        lastVal = turnSlot(3, slotNo)
        ser.write(bytes(lastVal))
        inputarr.append(lastVal)
        time.sleep(1)
        out = []
        while ser.in_waiting>0:
            out+=[ser.read(1).hex()]
        print(out)
        result.append(out)
        if(out[6:9] != ['03', '01', '00']):
            return result
        if(tryoutCnt < times):
            time.sleep(2)
        tryoutCnt += 1
    data['inputDesc'] = str(inputarr)
    return result

