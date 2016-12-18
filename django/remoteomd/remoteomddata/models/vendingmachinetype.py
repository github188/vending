from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings

predicateDict = {
    "VendingMachineType.user": "createdmachines"
}
class VendingMachineType(models.Model):
    DeliveryTypeChoice = (('spring', '弹簧'),('grid', '格子'),('Spr-Grid', '弹簧+格子'),)
    CashBoxType = (("NV11","NV11-ITL"),("NV9", "NV9-ITL"),)
    CoinBoxType = (("Hopper", "Hopper"),)
    MasterBoardType = (("1037F", "1037F"),)
    ControllerBoardType = (("Banma", "banma"),)
    MonitorType = (("Antel", "Antel"),)


    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["VendingMachineType.user"], default=1, verbose_name = "创建人")
    deliveryType = models.CharField("出货类型", max_length=20, choices = DeliveryTypeChoice);
    cashBoxType = models.CharField("钞箱", max_length=20, choices = CashBoxType)
    coinBoxType = models.CharField("硬币器", max_length=20, choices = CoinBoxType)
    masterBoardType = models.CharField("主板", max_length=20, choices = MasterBoardType)
    controllerBoardType = models.CharField("控制板", max_length=20, choices = ControllerBoardType)
    monitorType = models.CharField("显示器", max_length=20, choices = MonitorType);
    num_SpringSlot = models.PositiveSmallIntegerField("弹簧货道数", default=60, validators=[MinValueValidator(0), MaxValueValidator(1000)]);
    num_GridSlot = models.PositiveSmallIntegerField("格子数", default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)]);
    num_Cabinet = models.PositiveSmallIntegerField("柜子数", default=1, validators=[MinValueValidator(1), MaxValueValidator(20)]);
    class Meta:
        verbose_name = verbose_name_plural = "1. 售货机类型"

    def __str__(self):
        return self.deliveryType + '{:03d}'.format(self.id)
    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.slug})