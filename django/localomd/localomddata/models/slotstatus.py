from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from localomddata.models.product import Product
from localomddata.models.slot import Slot
from localomddata.models.vendingmachine import VendingMachine

predicateDict = {
    "SlotStatus.slot": "status",
    "SlotStatus.product": "status",
    "SlotStatus.user": "slotstatus",
}
class SlotStatus(models.Model):
    CurrentRunStatus = (
        ('1','正常'),
        ('0','故障'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["SlotStatus.user"], default=1, verbose_name = "创建人")
    runningStatus = models.CharField("运行状态", default="1", max_length=1, choices=CurrentRunStatus)
    slot = models.ForeignKey(Slot, related_name=predicateDict["SlotStatus.slot"], on_delete=models.CASCADE, verbose_name = "货道")
    currentItemNum = models.PositiveSmallIntegerField("当前数量", default=0, validators=[MinValueValidator(1), MaxValueValidator(200)])
    malfunctionReportCount = models.PositiveSmallIntegerField("故障计数", default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    product = models.ForeignKey(Product, related_name=predicateDict["SlotStatus.product"], on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "商品")
    createTime = models.DateTimeField("创建时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = "7. 货道状态记录"
    def __str__(self):
        return self.slot.slotNo