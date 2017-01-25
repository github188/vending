from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from localomddata.models.commonFields import CommonFields

predicateDict = {
    "CoinChange.user": "CoinChange",
}
class CoinChangeLog(CommonFields):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["CoinChange.user"], default=1, verbose_name = "创建人")
    amountBefore = models.PositiveSmallIntegerField("前余额", default=0);
    amountData = models.SmallIntegerField("当前数量", default=0);
    amountAfter = models.PositiveSmallIntegerField("后余额");
    class Meta:
        verbose_name = verbose_name_plural = "12. 硬币变更日志"
        ordering = ["-id",]

    def __str__(self):
        return str(self.id)

def pre_save_coinchange_receiver(sender, instance, *args, **kwargs):
    if not instance.amountAfter:
        instance.amountAfter = instance.amountBefore + instance.amountData


pre_save.connect(pre_save_coinchange_receiver, sender=CoinChangeLog)