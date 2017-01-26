from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from cashMachine.models.commonFields import CommonFields


class CashboxOperate(CommonFields):
    operateChoice = (
        ("toll", "收费"),
        ("terminate", "收费终止"),
        ("charge", "充零钱"),
        ("memberCharge", "会员充值"),
        ("clearPayout", "零钱清空"),
        ("payout", "找零"),
        ("currentPayoutAvailable", "可用零钱"),
    )
    operateName = models.CharField("操作名称", max_length=100, choices = operateChoice)
    operateData = models.PositiveSmallIntegerField("操作数", default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]);

    class Meta:
        verbose_name = verbose_name_plural = "1. 钞箱任务"
    def __str__(self):
        return str(self.id)
