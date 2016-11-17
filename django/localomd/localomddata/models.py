from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse

predicateDict = {
    "VendingMachineType.creator": "createdmachines"
    ,"VendingMachine.charger": "chargingmachines"
    , "VendingMachine.vmType": "machines"
    , "VendingMachine.productCategory": "machines"
    ,"ProductCategory.parent": "children"
    ,"Product.provider": "products"
    ,"Product.orderByUser":"orderedProducts"
    ,"Product.category":"products"
    ,"Slot.vmSlug": "slots"
    ,"Slot.product": "slots"
    ,"MoneyCharge.user": "userCharges"
    ,"MoneyCharge.vmSlug": "vmCharges"
    ,"OrderMain.slot": "orders"

}

class VendingMachineType(models.Model):
    DeliveryTypeChoice = (('spring', '弹簧'),('grid', '格子'),('Spr-Grid', '弹簧+格子'),)
    CashBoxType = (("NV11","NV11-ITL"),("NV9", "NV9-ITL"),)
    CoinBoxType = (("Hopper", "Hopper"),)
    MasterBoardType = (("1037F", "1037F"),)
    ControllerBoardType = (("Banma", "banma"),)
    MonitorType = (("Antel", "Antel"),)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["VendingMachineType.creator"], default=1, verbose_name = "创建人")
    deliveryType = models.CharField("出货类型", max_length=20, choices = DeliveryTypeChoice);
    cashBoxType = models.CharField("钞箱", max_length=20, choices = CashBoxType)
    coinBoxType = models.CharField("硬币器", max_length=20, choices = CoinBoxType)
    masterBoardType = models.CharField("主板", max_length=20, choices = MasterBoardType)
    controllerBoardType = models.CharField("控制板", max_length=20, choices = ControllerBoardType)
    monitorType = models.CharField("显示器", max_length=20, choices = MonitorType);
    num_SpringSlot = models.PositiveSmallIntegerField("弹簧货道数", default=64);
    num_GridSlot = models.PositiveSmallIntegerField("格子数", default=0);
    num_Cabinet = models.PositiveSmallIntegerField("柜子数", default=1);
    class Meta:
        verbose_name = verbose_name_plural = "1. 售货机类型"

    def __str__(self):
        return self.deliveryType + '-' + str(self.id)
    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.slug})

class ProductCategory(models.Model):
    catName = models.CharField("分类名", max_length=20)
    slug = models.CharField("编辑名", max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True, related_name=predicateDict["ProductCategory.parent"], verbose_name = "父类")
    class Meta:
        verbose_name = verbose_name_plural = "4. 商品类别"
    def __str__(self):
        return self.catName
#########################################################################################################
class VendingMachine(models.Model):
    slug = models.CharField("编号", max_length=120, unique=True)
    vmType = models.ForeignKey(VendingMachineType, verbose_name="售货机类型", related_name=predicateDict['VendingMachine.vmType'])
    charger = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name=predicateDict["VendingMachine.charger"], verbose_name = "负责人");
    productCategory = models.ManyToManyField(ProductCategory, related_name=predicateDict["VendingMachine.productCategory"], verbose_name="商品分类")
    chargerTel = models.CharField("联系电话", max_length=11);
    installAddress = models.CharField("安装地址", max_length=240, unique=True);
    installTime = models.DateTimeField("安装时间", auto_now_add=False, auto_now=False)
    aliveTime = models.DateTimeField("运行开始时间", auto_now_add=False, auto_now=False)
    class Meta:
        verbose_name = verbose_name_plural = "2. 售货机"
    def __str__(self):
        return self.slug


def createVmSlug(instance):
    slugPrefix = instance.charger.username + '-' + str(instance.vmType) + '-'
    qs = VendingMachine.objects.filter(slug__startswith = slugPrefix).order_by("-id")
    if qs.exists():
        slug = "%s-%s" %(slugPrefix, qs.first().id+1)
    else:
        slug=slugPrefix+'1'
    return slug

def pre_save_vm_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = createVmSlug(instance)

pre_save.connect(pre_save_vm_receiver, sender=VendingMachine)

##########################################################################################
class ProductProvider(models.Model):
    companyName = models.CharField("公司名", max_length=120, unique=True)
    contactName = models.CharField("联系人名", max_length=120)
    contactTel = models.CharField("联系电话", max_length=11, null = True)
    siteUrl = models.URLField("站点地址", null=True, unique=True)
    class Meta:
        verbose_name = verbose_name_plural = "3. 产品供应"
    def __str__(self):
        return self.companyName

##############################################################################################
class Product(models.Model):
    OrderCountUnit = (
        ("piece", "个"),
        ("package", "包"),
        ("case", "盒"),
        ("kilogram", "公斤"),
        ("batch", "批次"),
    )
    provider = models.ForeignKey(ProductProvider, related_name=predicateDict["Product.provider"], on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "供应商" )
    orderPrice = models.PositiveSmallIntegerField("订购单价", default=90);
    orderTotalPrice = models.PositiveSmallIntegerField("订购总价", default=900);
    orderCount = models.PositiveSmallIntegerField("订购数量", default=1);
    orderCountUnit = models.CharField("订购单位", max_length=20, choices = OrderCountUnit)
    orderTime = models.DateTimeField("订购时间", auto_now = False, auto_now_add=True)
    orderByUser =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Product.orderByUser"],  default=1, verbose_name = "采购人")
    imageRefUrl = models.URLField("图片参考", null=True)
    imageListUrl = models.URLField("列表图", null=True)
    imageDetailUrl = models.URLField("详情图", null=True)
    isActive = models.BooleanField("生效", default=False)
    productName = models.CharField("名称", max_length=120)
    productSumary = models.CharField("摘要", max_length=500)
    productDesc = models.CharField("详细", max_length=1000)
    productPrice =  models.PositiveSmallIntegerField("售价", default=100);
    productBarUrl = models.URLField("支付条码地址", null=True)
    category = models.ManyToManyField(ProductCategory, related_name=predicateDict["Product.category"], verbose_name= "分类")
    class Meta:
        verbose_name = verbose_name_plural = "5. 商品详细"
    def __str__(self):
        return self.productName

def createProductOrderTotalPrice(instance):
        return instance.orderPrice * instance.orderCount

def pre_save_product_receiver(sender, instance, *args, **kwargs):
        if not instance.orderTotalPrice:
            instance.orderTotalPrice = createProductOrderTotalPrice(instance)

pre_save.connect(pre_save_product_receiver, sender=Product)

################################################################################################
class Slot(models.Model):
    ControllType = (
        ('spring', '弹簧'),
        ('grid', '格子'),
    )
    vmSlug = models.ForeignKey(VendingMachine, related_name=predicateDict["Slot.vmSlug"], on_delete=models.CASCADE, verbose_name = "售货机编号")
    slotNo = models.CharField("货道编号", max_length=120, unique=True)
    capacity = models.PositiveSmallIntegerField("货道容量", default=1);
    controllType = models.CharField("驱动类型", max_length=20, choices=ControllType)
    currentItemNum = models.PositiveSmallIntegerField("当前数量", default=0)
    malfunctionReportCount = models.PositiveSmallIntegerField("故障计数", default=0)
    product = models.ForeignKey(Product, related_name=predicateDict["Slot.vmSlug"], on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "商品")
    class Meta:
        verbose_name = verbose_name_plural = "6. 货道详细"
    def __str__(self):
        return self.slotNo

class MoneyCharge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["MoneyCharge.user"], default=1, verbose_name = "创建人")
    vmSlug = models.ForeignKey(VendingMachine, related_name=predicateDict["MoneyCharge.vmSlug"], on_delete=models.CASCADE, verbose_name="售货机编号")
    cashAmount = models.DecimalField("10元金额", default=1, max_digits=3, decimal_places=0)
    coinAmount = models.DecimalField("一元硬币金额", default=1, max_digits=3, decimal_places=0)
    totalAmount = models.DecimalField("合计金额", default=1, max_digits=3, decimal_places=0)
    createTime = models.DateTimeField("发生时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)  #, null=True
    class Meta:
        verbose_name = verbose_name_plural = "7. 充值记录"
    def __str__(self):
        return str(self.vmSlug) + '  '+ str(self.cashAmount)+ '  ' + str(self.coinAmount)

def createTotalAmount(instance):
    return instance.cashAmount + instance.coinAmount

def pre_save_MoneyCharge_receiver(sender, instance, *args, **kwargs):
    if not instance.totalAmount:
        instance.totalAmount = createTotalAmount(instance)

pre_save.connect(pre_save_MoneyCharge_receiver, sender = MoneyCharge)

class OrderMain(models.Model):
    PayType = {
        ("0","cash"),("1","wechat")
    }
    slot = models.ForeignKey(Slot, related_name="orders", on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "货道")
    orderNo = models.CharField("订单号", max_length=1, choices=PayType, default="0", unique=True)
    payType = models.CharField("支付类型", max_length=1, choices=PayType,default="0")
    totalPaid = models.DecimalField("支付金额", default=1, max_digits=3, decimal_places=0)
    orderTime = models.DateTimeField("下单时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = verbose_name_plural = "8. 订单查看"
    def __str__(self):
        return self.orderNo

