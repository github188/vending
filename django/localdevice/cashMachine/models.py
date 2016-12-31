from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CashMachineManager(models.Manager):
    def byName(self, *args, **kwargs):
        return super(CashMachineManager, self).filter(operateName=args[0])
    def byPeriod(self, *args):
        return super(CashMachineManager, self).filter(operateTime__gte=args[0]).filter(orderTime__lte=args[1])

class CashboxOperate(models.Model):
    operateChoice = (
        ("toll", "收费"),
        ("terminate", "收费终止"),
        ("charge", "充零钱"),
        ("clearPayout", "零钱清空"),
        ("payout", "找零"),
        ("currentPayoutAvailable", "可用零钱"),
    )
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    operateName = models.CharField("操作名称", max_length=100, choices = operateChoice)
    operateData = models.PositiveSmallIntegerField("操作数", default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]);

    class Meta:
        verbose_name = verbose_name_plural = "1. 钞箱任务"
    def __str__(self):
        return str(self.id)

class CashboxLog(models.Model):
    operateState = (
        ("processing", "进行中"),
        ("succeed", "成功"),
        ("failed", "失败"),
        ("terminated", "终止")
    )
    operate = models.ForeignKey(CashboxOperate, related_name="logs", on_delete=models.CASCADE, blank=True, null=True, verbose_name = "操作" )
    operateStatus = models.CharField("状态", max_length=100, choices = operateState)
    retData = models.PositiveSmallIntegerField("返回数据", default=0);
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = verbose_name_plural = "2,钞箱日志"
        ordering = ["-id",]

    def __str__(self):
        return str(self.id)
