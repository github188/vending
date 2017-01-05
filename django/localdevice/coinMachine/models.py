from django.db import models

from datetime import date, datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class CoinChargeLog(models.Model):
    retData = models.PositiveSmallIntegerField("当前数量", default=0);
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = verbose_name_plural = "1,硬币日志"
        ordering = ["-id",]

    def __str__(self):
        return str(self.id)
