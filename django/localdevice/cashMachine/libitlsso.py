#docs.python.org/3/library/ctypes.html
import ast
from ctypes import *

import time

from pip._vendor import requests


class SSP_FULL_KEY(Structure):
    _fields_ = [("FixedKey", c_ulonglong),("EncryptKey", c_ulonglong)]


#ref docs.python.org/3/library/ctypes.html
class SSP_COMMAND(Structure):
    _fields_ = [("Key", SSP_FULL_KEY)
    ,("BaudRate", c_ulong)
    ,("Timeout", c_ulong)
    ,("PortNumber", c_ubyte)
    ,("SSPAddress", c_ubyte)
    ,("RetryLevel", c_ubyte)
    ,("EncryptionStatus", c_ubyte)
    ,("CommandDataLength", c_ubyte)
    ,("CommandData", c_ubyte*255)
    ,("ResponseStatus", c_ubyte)
    ,("ResponseDataLength", c_ubyte)
    ,("ResponseData", c_ubyte*255)
    ,("IgnoreError", c_ubyte)]

def getConfLocation():
    session  = requests.Session()
    session.trust_env = False #disable proxy
    response1 = session.get('http://172.18.0.4/api/data/config/?format=json&confname=libsso')
    response2 = session.get('http://172.18.0.4/api/data/config/?format=json&confname=cashmachine')
    address = ast.literal_eval(response1.text)[0]["confvalue"]
    portNo = ast.literal_eval(response2.text)[0]["confvalue"].encode()
    return address, portNo

class LibItlSSO():

    def __init__(self):
        self.conf = getConfLocation()
        # address1 = "/home/pjsong/Documents/git/bitbucket/itl-validator/libBasicValidator/Debug/libbasicvalidator.so"
        self.libBasicValidator = CDLL(self.conf[0])
        self.sspCommand = byref(SSP_COMMAND())
        self.initRet = self.libBasicValidator.omd_init_validator(self.conf[1], self.sspCommand)
        print("libitlsso  initRet:%d" % (self.initRet))

    def checkInitRet(self):
        tryCnt = 10
        while(self.initRet<0 and tryCnt>0):
            tryCnt -=1
            # b'/dev/ttyACM0'
            self.initRet = self.libBasicValidator.omd_init_validator(self.conf[1], self.sspCommand)
        if(self.initRet<0):
            return -1
        return 1

    def configValidator(self, totalAmount):
        if(self.checkInitRet()<0):
            return -1;
        tryCnt = 10
        confRet = self.libBasicValidator.omd_config_validator(self.sspCommand, c_char(0x04), totalAmount)
        while(confRet < 0 and tryCnt>0):
            confRet = self.libBasicValidator.omd_config_validator(self.sspCommand, c_char(0x04), totalAmount)
            tryCnt -= 1
        if(confRet<0):
            return -2;
        return 1
    # def channelCnt(self):
    #     ret = self.libBasicValidator.omd_payout_channel_available_cnt(self.sspCommand)
    #     print("libitlsso available channel count: %d" % ret)
    #     return ret;

    def payoutNote(self):
        if(self.checkInitRet()<0):
            return -1;
        ret = self.libBasicValidator.payoutOneNote(self.sspCommand)
        print("payout result of libitlsso.py: %d" % ret)
        return ret

    def setRunningStatusToFalse(self):
        if(self.checkInitRet()<0):
            return -1;
        return self.libBasicValidator.disableValidator(self.sspCommand)

    def creditOne(self, timeoutInSeconds):
        if(self.checkInitRet()<0):
            return -1;
        return self.libBasicValidator.creditOneNote(self.sspCommand, timeoutInSeconds)

    # def tollOneByOne(self, amountToDo):
    #     self.config(self, amountToDo)
    #     while amountToDo > 0:
    #         creditNoteValue = self.creditOne()
    #         amountToDo -= creditNoteValue
    #         if (creditNoteValue == 0):
    #             break;

    # def toll(self, amount):
    #     tollRet = self.libBasicValidator.omd_toll_loop(self.sspCommand, amount)
    #     print("toll ret: %d " % tollRet)
    #     return tollRet

    def charge(self, amount):
        if(self.checkInitRet()<0):
            return -1;
        tollRet = self.libBasicValidator.omd_charge_loop(self.sspCommand, amount)
        print("libitlsso toll ret: %d " % tollRet)
        return tollRet

    def payoutCnt(self):
        if(self.checkInitRet()<0):
            return -1;
        payoutRet = self.libBasicValidator.omd_payout_note_available_cnt(self.sspCommand)
        print("libitlsso  payout cnt: %d " % payoutRet)
        return payoutRet

    def emptyStore(self):
        emptiedAmount = self.libBasicValidator.omd_3F_empty_store(self.sspCommand)
        return emptiedAmount

    def closePort(self):
        self.libBasicValidator.close_ssp_port()