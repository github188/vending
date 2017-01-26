from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from remoteomddata.models.vendingmachine import VendingMachine

class MoneyChargeManager(models.Manager):
    def byTotalAmount(self, *args, **kwargs):
        return super(MoneyChargeManager, self).filter(totalAmount=args[0])
    def byPeriod(self, *args):
        return super(MoneyChargeManager, self).filter(createTime__gte=args[0]).filter(createTime__lte=args[1])


predicateDict = {
    "MoneyCharge.user": "userCharges"
    ,"MoneyCharge.vmSlug": "vmCharges"
}
class MoneyCharge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["MoneyCharge.user"], default=1, verbose_name = "创建人")
    vmSlug = models.ForeignKey(VendingMachine, related_name=predicateDict["MoneyCharge.vmSlug"], on_delete=models.CASCADE, verbose_name="售货机编号")
    cashAmount = models.DecimalField("10元金额", default=1, max_digits=3, decimal_places=0)
    coinAmount = models.DecimalField("一元硬币金额", default=1, max_digits=3, decimal_places=0)
    totalAmount = models.DecimalField("合计金额",max_digits=3, decimal_places=0)
    createTime = models.DateTimeField("发生时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)  #, null=True
    class Meta:
        verbose_name = verbose_name_plural = "08. 充值记录"
    def __str__(self):
        return str(self.vmSlug) + '  '+ str(self.cashAmount)+ '  ' + str(self.coinAmount)

def createTotalAmount(instance):
    return instance.cashAmount + instance.coinAmount

def pre_save_MoneyCharge_receiver(sender, instance, *args, **kwargs):
    if not instance.totalAmount:
        instance.totalAmount = createTotalAmount(instance)

pre_save.connect(pre_save_MoneyCharge_receiver, sender = MoneyCharge)