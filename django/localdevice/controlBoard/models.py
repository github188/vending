from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ControlBoardManager(models.Manager):
    def byName(self, *args, **kwargs):
        return super(ControlBoardManager, self).filter(productName=args[0])
    def byPeriod(self, *args):
        return super(ControlBoardManager, self).filter(orderTime__gte=args[0]).filter(orderTime__lte=args[1])


predicateDict = {
     "ControlBoardOutput.inputId": "inputId"
}


class ControlBoardInput(models.Model):
    turnCnt = models.PositiveSmallIntegerField("循环计数", default=1, validators=[MaxValueValidator(60), MinValueValidator(1)])
    slotNo =  models.PositiveSmallIntegerField("货道编号", default=1, validators=[MaxValueValidator(60), MinValueValidator(0)])
    inputDesc = models.CharField("详细", max_length=1000)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = verbose_name_plural = "2. 输入详细"
    def __str__(self):
        return self.inputDesc

class ControlBoardOutput(models.Model):
    input = models.ForeignKey(ControlBoardInput, related_name=predicateDict["ControlBoardOutput.inputId"], on_delete=models.CASCADE, verbose_name = "输入ID" )
    outputDesc = models.CharField("详细", max_length=1000)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = verbose_name_plural = "2. 输出详细"
    def __str__(self):
        return self.outputDesc
