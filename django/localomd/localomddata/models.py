from django.db import models
from django.conf import settings

class VendingMachine(models.Model):
    VmTypeChoice = (
        ('spring', '弹簧'),
        ('grid', '格子'),
        ('Spr-Grid', '弹簧+格子'),
    )
    CashBoxType = (
        ("NV11","NV11-ITL"),
        ("NV9", "NV9-ITL"),
    )
    CoinBoxType = (
        ("Hopper", "Hopper"),
    )
    MasterBoardType = (
        ("1037F", "1037F"),
    )
    ControllerBoardType = (
        ("Banma", "banma"),
    )
    MonitorType = (
        ("Antel", "Antel"),
    )

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name = "创建人")
    vmSku = models.CharField("编号", max_length=120, unique=True)
    vmType = models.CharField("类型", max_length=20, choices = VmTypeChoice);
    cashBoxType = models.CharField("钞箱", max_length=20, choices = CashBoxType)
    coinBoxType = models.CharField("硬币器", max_length=20, choices = CoinBoxType)
    masterBoardType = models.CharField("主板", max_length=20, choices = MasterBoardType)
    controllerBoardType = models.CharField("控制板", max_length=20, choices = ControllerBoardType)
    monitorType = models.CharField("显示器", max_length=20, choices = MonitorType);
    num_SpringSlot = models.PositiveSmallIntegerField("弹簧货道数", default=64);
    num_GridSlot = models.PositiveSmallIntegerField("格子数", default=0);
    num_Cabinet = models.PositiveSmallIntegerField("柜子数", default=1);
    charger = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name="charger", verbose_name = "负责人");
    chargerTel = models.CharField("联系电话", max_length=11);
    installAddress = models.CharField("安装地址", max_length=240, unique=True);
    class Meta:
        verbose_name = verbose_name_plural = "1. 售货机"

    def __str__(self):
        return self.vmSku


class ProductProvider(models.Model):
    companyName = models.CharField("公司名", max_length=120, unique=True)
    contactName = models.CharField("联系人名", max_length=120, unique=True)
    contactTel = models.CharField("联系电话", max_length=11, null = True)
    siteUrl = models.URLField("站点地址", null=True)
    class Meta:
        verbose_name = verbose_name_plural = "2. 产品供应"
    def __str__(self):
        return self.companyName

class ProductCategory(models.Model):
    vmSku = models.ForeignKey(VendingMachine, on_delete=models.CASCADE, verbose_name = "售货机编号")
    catName = models.CharField("分类名", max_length=20)
    slug = models.CharField("编辑名", max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name = "父类")
    class Meta:
        verbose_name = verbose_name_plural = "3. 商品类别"
    def __str__(self):
        return self.catName


class Product(models.Model):
    OrderCountUnit = (
        ("piece", "个"),
        ("package", "包"),
        ("case", "盒"),
        ("kilogram", "公斤"),
    )
    provider = models.ForeignKey(ProductProvider, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "供应商" )
    orderPrice = models.PositiveSmallIntegerField("订购单价", default=90);
    orderTotalPrice = models.PositiveSmallIntegerField("订购总价", default=900);
    orderCount = models.PositiveSmallIntegerField("订购数量", default=1);
    orderCountUnit = models.CharField("订购单位", max_length=20, choices = OrderCountUnit)
    orderTime = models.DateTimeField("订购时间", auto_now = False, auto_now_add=True)
    orderByUser =  models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name = "采购人")
    imageRefUrl = models.URLField("图片参考", null=True)
    imageListUrl = models.URLField("列表图", null=True)
    imageDetailUrl = models.URLField("详情图", null=True)
    isActive = models.BooleanField("生效", default=False)
    productName = models.CharField("名称", max_length=120)
    productSumary = models.CharField("摘要", max_length=500)
    productDesc = models.CharField("详细", max_length=1000)
    productPrice =  models.PositiveSmallIntegerField("售价", default=100);
    productBarUrl = models.URLField("支付条码地址", null=True)
    category = models.ManyToManyField(ProductCategory, verbose_name= "分类")
    class Meta:
        verbose_name = verbose_name_plural = "4. 商品详细"
    def __str__(self):
        return self.productName

class Slot(models.Model):
    ControllType = (
        ('spring', '弹簧'),
        ('grid', '格子'),
    )
    vmSku = models.ForeignKey(VendingMachine, on_delete=models.CASCADE, verbose_name = "售货机编号")
    slotNo = models.CharField("货道编号", max_length=120, unique=True)
    capacity = models.PositiveSmallIntegerField("货道容量", default=1);
    controllType = models.CharField("驱动类型", max_length=20, choices=ControllType)
    currentItemNum = models.PositiveSmallIntegerField("当前数量", default=0)
    malfunctionReportCount = models.PositiveSmallIntegerField("故障计数", default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "商品")
    class Meta:
        verbose_name = verbose_name_plural = "5. 货道详细"
    def __str__(self):
        return self.slotNo


class OrderMain(models.Model):
    PayType = {
        ("0","cash"),("1","wechat")
    }
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "货道")
    orderNo = models.CharField("订单号", max_length=1, choices=PayType, default="0", unique=True)
    payType = models.CharField("支付类型", max_length=1, choices=PayType,default="0")
    totalPaid = models.DecimalField("支付金额", default=1, max_digits=3, decimal_places=0)
    orderTime = models.DateTimeField("下单时间", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = verbose_name_plural = "6. 订单查看"
    def __str__(self):
        return self.orderNo