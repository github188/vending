from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

from django.db.models.signals import pre_save

from localomddata.models.product import Product
from localomddata.models.slot import Slot


class OrderMainManager(models.Manager):
    def submitted(self, *args, **kwargs):
        return super(OrderMainManager, self).filter(status='0')
    def finished(self):
        return super(OrderMainManager, self).filter(status='2')
    def byOrderNo(self, *args):
        return super(OrderMainManager, self).filter(orderNo=args[0])



predicateDict = {
    "OrderMain.slot": "orders", "OrderMain.user": "orders"
}
PayType = {
    ("0", "现金"), ("1", "会员"),("3","微信"),("4", "支付宝")
}
Status = {
    ("0", "已提交"), ("1", "已支付"),("2", "已完成")
}


def createOrderNo(instance):
    thisday = datetime.date.today();
    orderPrefix = '{:02d}'.format(thisday.month)+'{:02d}'.format(thisday.day)
    qs = OrderMain.objects.filter(orderNo__startswith=orderPrefix).order_by("-orderNo")
    if qs.exists():
        orderNo = "%s" % (int(qs.first().orderNo) + 1)
    else:
        orderNo = orderPrefix + '0000'
    return orderNo

class OrderMain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["OrderMain.user"], default=1, verbose_name = "创建人")
    slot = models.ForeignKey(Slot, related_name="orders", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "货道")
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "商品")
    itemCount = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(64), MinValueValidator(1)])
    orderNo = models.CharField("订单号", max_length=8, default=createOrderNo)
    payType = models.CharField("支付类型", max_length=1, choices=PayType, default="0")
    status = models.CharField("订单状态", max_length=1, choices=Status, default = '0')
    totalPaid = models.DecimalField("支付金额", max_digits=3, decimal_places=0)
    createTime = models.DateTimeField("下单时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = verbose_name_plural = "09. 订单查看"
    def __str__(self):
        return self.orderNo



def createTotalPaid(instance):
    product = Product.objects.get(pk=instance.product.id)
    return product.saleUnitPrice * instance.itemCount;

def pre_save_vm_receiver(sender, instance, *args, **kwargs):
    if not instance.orderNo:
        instance.orderNo = createOrderNo(instance)
    if not instance.totalPaid:
        instance.totalPaid = createTotalPaid(instance)


pre_save.connect(pre_save_vm_receiver, sender=OrderMain)