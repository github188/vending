from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from localomddata.models.product import Product
from localomddata.models.vendingmachine import VendingMachine

predicateDict = {
    "Slot.vmSlug": "slots"
    ,"Slot.product": "slots"
    ,"Slot.user": "slots"

}
class Slot(models.Model):
    ControllType = (
        ('spring', '弹簧'),
        ('grid', '格子'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Slot.user"], default=1, verbose_name = "创建人")

    vendingMachine = models.ForeignKey(VendingMachine, related_name=predicateDict["Slot.vmSlug"], on_delete=models.CASCADE, verbose_name = "售货机编号")
    slotNo = models.CharField("货道编号", max_length=120, unique=True)
    capacity = models.PositiveSmallIntegerField("货道容量", default=1, validators=[MinValueValidator(1), MaxValueValidator(200)]);
    controllType = models.CharField("驱动类型", max_length=20, choices=ControllType)
    class Meta:
        verbose_name = verbose_name_plural = "6. 货道详细"
    def __str__(self):
        return str(self.id)