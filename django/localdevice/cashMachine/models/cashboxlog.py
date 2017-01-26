from datetime import date, datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from cashMachine.models.cashboxoperate import CashboxOperate
from cashMachine.models.commonFields import CommonFields


class CashboxLog(CommonFields):
    operateState = (
        ("processing", "进行中"),
        ("succeed", "成功"),
        ("failed", "失败"),
        ("terminated", "终止")
    )
    operate = models.ForeignKey(CashboxOperate, related_name="logs", on_delete=models.CASCADE, blank=True, null=True, verbose_name = "操作" )
    operateStatus = models.CharField("状态", max_length=100, choices = operateState)
    retData = models.PositiveSmallIntegerField("返回数据", default=0);
    class Meta:
        verbose_name = verbose_name_plural = "2,钞箱日志"
        ordering = ["-id",]

    def __str__(self):
        return str(self.id)


predicateDict = {
    "OrderMain.slot": "orders", "OrderMain.user": "orders"
}
PayType = {
    ("0", "cash"), ("1", "wechat")
}
Status = {
    ("0", "submitted"), ("1", "paid"),("2", "received")
}

