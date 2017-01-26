from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
class UnSyncedManager(models.Manager):
    def get_querySet(self):
        return super(UnSyncedManager, self).get_queryset().filter(self.sendFlag > '1')
"""
  for most common fields
"""
class CommonFields(models.Model):
    #sendFlag is the num of binary, each bit is a system, for sending.
    # different value mapped by different sync task, unless it's changed to 1.
    sendFlag = models.PositiveSmallIntegerField("发送标志", default=2)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)

    objects = models.Manager()
    unsynced_objects = UnSyncedManager()

    class Meta:
        abstract = True


class CoinMachineInput(CommonFields):
    payoutCnt =  models.PositiveSmallIntegerField("吐币数", default=1, validators=[MaxValueValidator(9), MinValueValidator(0)])
    inputDesc = models.CharField("详细", default="", null=True, max_length=30)
    class Meta:
        verbose_name = verbose_name_plural = "1. 输入详细"
    def __str__(self):
        return str(self.id)

predicateDict = {
     "CoinMachineOutput.inputId": "inputId"
}

class CoinMachineOutput(CommonFields):
    input = models.ForeignKey(CoinMachineInput, related_name=predicateDict["CoinMachineOutput.inputId"], on_delete=models.CASCADE, verbose_name = "输入ID" )
    outputDesc = models.CharField("详细", max_length=30)

    class Meta:
        verbose_name = verbose_name_plural = "2. 输出详细"
    def __str__(self):
        return self.outputDesc