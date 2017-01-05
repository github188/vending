from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

from django.db.models.signals import pre_save

class OrderMainManager(models.Manager):
    def submitted(self, *args, **kwargs):
        return super(OrderMainManager, self).filter(status='0')
    def finished(self):
        return super(OrderMainManager, self).filter(status='2')
    def byOrderNo(self, *args):
        return super(OrderMainManager, self).filter(orderNo=args[0])
    def createOrderMain(self, user=1, slot = None, product = None, itemCount=1, paytype=0, status=2, totalpaid=0):
        om = self.create(user=user, slot=slot, product=product, itemCount = itemCount, paytype=paytype, status=status, totalpaid = totalpaid)
        return om

predicateDict = {
    "OrderMain.slot": "orders", "OrderMain.user": "orders"
}
PayType = {
    ("0", "现金"), ("1", "会员"),("3","微信"),("4", "支付宝")
}
Status = {
    ("0", "已提交"), ("1", "已支付"),("2", "已完成")
}
def createOrderNo():
    thisday = datetime.date.today();
    orderPrefix = '{:02d}'.format(thisday.month)+'{:02d}'.format(thisday.day)
    qs = OrderMain.objects.filter(orderNo__startswith=orderPrefix).order_by("-id")
    if qs.exists():
        orderNo = orderPrefix + "%04d" % (int(qs.first().orderNo[4:]) + 1)
    else:
        orderNo = orderPrefix + '0000'
    return orderNo


class OrderMain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["OrderMain.user"], default=1, verbose_name = "创建人")
    slot = models.CharField("货道Id", max_length=120, blank=True, null=True)
    product = models.CharField("商品Id", max_length=120, blank=True, null=True)
    itemCount = models.PositiveSmallIntegerField("数量", default=1, validators=[MaxValueValidator(64), MinValueValidator(1)])
    orderNo = models.CharField("订单号", max_length=8, default=createOrderNo)
    payType = models.CharField("支付类型", max_length=1, choices=PayType, default='0')
    status = models.CharField("订单状态", max_length=1, choices=Status, default = '2')
    totalPaid = models.DecimalField("支付金额", max_digits=3, decimal_places=0)
    changeLeft = models.PositiveSmallIntegerField("纸币余额", default=-1)
    coinLeft = models.PositiveSmallIntegerField("硬币余额", default=-1)
    createTime = models.DateTimeField("下单时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = verbose_name_plural = "3. 订单查看"
    def __str__(self):
        return str(self.id)

    objects = OrderMainManager()



# def createTotalPaid(instance):
#     product = Product.objects.get(pk=instance.product.id)
#     return product.saleUnitPrice * instance.itemCount;

def pre_save_vm_receiver(sender, instance, *args, **kwargs):
    print(instance.orderNo)
    if not instance.orderNo:
        instance.orderNo = createOrderNo(instance)


pre_save.connect(pre_save_vm_receiver, sender=OrderMain)



# def getOrderNo():
#     year = int(str(datetime.now().year)[2:])
#     month = datetime.now().month
#     day = datetime.now().day
#     hour = datetime.now().hour
#     minute = datetime.now().minute
#     seconds = datetime.now().second
#     return "%02d-%02d-%02d-%02d%02d%02d" % (month, day, year, hour, minute, seconds)
#
#
# def pre_save_order_receiver(sender, instance, *args, **kwargs):
#     if (instance.user.name):
#             instance.orderNo = instance.orderNo +'_'+ instance.user.name
#
# pre_save.connect(pre_save_order_receiver, sender=OrderMain)
