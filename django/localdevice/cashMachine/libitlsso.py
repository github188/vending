#docs.python.org/3/library/ctypes.html

from ctypes import *

import time


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

class LibItlSSO():

    def __init__(self):
        address1 = "/home/pjsong/Documents/git/bitbucket/itl-validator/libBasicValidator/Debug/libbasicvalidator.so"
        self.libBasicValidator = CDLL(address1)
        self.sspCommand = byref(SSP_COMMAND())
        self.initRet = self.libBasicValidator.omd_init_validator(b'/dev/ttyUSB0', self.sspCommand)
        print("libitlsso  initRet:%d" % (self.initRet))


    def configValidator(self, totalAmount):
        self.libBasicValidator.omd_config_validator(self.sspCommand, c_char(0x04), totalAmount)

    # def channelCnt(self):
    #     ret = self.libBasicValidator.omd_payout_channel_available_cnt(self.sspCommand)
    #     print("libitlsso available channel count: %d" % ret)
    #     return ret;

    def payoutNote(self):
        ret = self.libBasicValidator.payoutOneNote(self.sspCommand)
        print("payout result of libitlsso.py: %d" % ret)
        return ret

    def setRunningStatusToFalse(self):
        return self.libBasicValidator.disableValidator(self.sspCommand)

    def creditOne(self, timeoutInSeconds):
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
        tollRet = self.libBasicValidator.omd_charge_loop(self.sspCommand, amount)
        print("libitlsso toll ret: %d " % tollRet)
        return tollRet

    def payoutCnt(self):
        payoutRet = self.libBasicValidator.omd_payout_note_available_cnt(self.sspCommand)
        print("libitlsso  payout cnt: %d " % payoutRet)
        return payoutRet

    def emptyStore(self):
        emptiedAmount = self.libBasicValidator.omd_3F_empty_store(self.sspCommand)
        return emptiedAmount

    def closePort(self):
        self.libBasicValidator.close_ssp_port()