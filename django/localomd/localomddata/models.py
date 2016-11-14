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

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    vmSku = models.CharField(max_length=120, unique=True)
    vmType = models.CharField(max_length=20, choices = VmTypeChoice);
    cashBoxType = models.CharField(max_length=20, choices = CashBoxType)
    coinBoxType = models.CharField(max_length=20, choices = CoinBoxType)
    masterBoardType = models.CharField(max_length=20, choices = MasterBoardType)
    controllerBoardType = models.CharField(max_length=20, choices = ControllerBoardType)
    monitorType = models.CharField(max_length=20, choices = MonitorType);
    num_SpringSlot = models.PositiveSmallIntegerField(default=64);
    num_GridSlot = models.PositiveSmallIntegerField(default=0);
    num_Cabinet = models.PositiveSmallIntegerField(default=1);
    charger = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name="charger");
    chargerTel = models.CharField(max_length=11);
    installAddress = models.CharField(max_length=240, unique=True);
    class Meta:
        verbose_name_plural = "1. 售货机"

    def __str__(self):
        return self.vmSku


class ProductProvider(models.Model):
    companyName = models.CharField(max_length=120, unique=True)
    contactName = models.CharField(max_length=120, unique=True)
    contactTel = models.CharField(max_length=11, null = True)
    siteUrl = models.URLField(null=True)
    class Meta:
        verbose_name_plural = "2. 产品供应"
    def __str__(self):
        return self.companyName

class ProductCategory(models.Model):
    vmSku = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    catName = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True)
    class Meta:
        verbose_name_plural = "3. 商品类别"
    def __str__(self):
        return self.catName


class Product(models.Model):
    OrderCountUnit = (
        ("piece", "个"),
        ("package", "包"),
        ("case", "盒"),
        ("kilogram", "公斤"),
    )
    provider = models.ForeignKey(ProductProvider, on_delete=models.SET_NULL, blank=True, null=True )
    orderPrice = models.PositiveSmallIntegerField(default=90);
    orderTotalPrice = models.PositiveSmallIntegerField(default=900);
    orderCount = models.PositiveSmallIntegerField(default=1);
    orderCountUnit = models.CharField(max_length=20, choices = OrderCountUnit)
    orderTime = models.DateTimeField(auto_now = False, auto_now_add=True)
    orderByUser =  models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    imageRefUrl = models.URLField(null=True)
    imageListUrl = models.URLField(null=True)
    imageDetailUrl = models.URLField(null=True)
    isActive = models.BooleanField(default=False)
    productName = models.CharField(max_length=120)
    productSumary = models.CharField(max_length=500)
    productDesc = models.CharField(max_length=1000)
    productPrice =  models.PositiveSmallIntegerField(default=100);
    productBarUrl = models.URLField(null=True)
    category = models.ManyToManyField(ProductCategory)
    class Meta:
        verbose_name_plural = "4. 商品详细"
    def __str__(self):
        return self.productName

class Slot(models.Model):
    ControllType = (
        ('spring', '弹簧'),
        ('grid', '格子'),
    )
    vmSku = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    slotNo = models.CharField(max_length=120, unique=True)
    capacity = models.PositiveSmallIntegerField(default=1);
    controllType = models.CharField(max_length=20, choices=ControllType)
    currentItemNum = models.PositiveSmallIntegerField(default=0)
    malfunctionReportCount = models.PositiveSmallIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        verbose_name_plural = "5. 货道详细"
    def __str__(self):
        return self.slotNo


class OrderMain(models.Model):
    PayType = {
        ("0","cash"),("1","wechat")
    }
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, blank=True, null=True)
    orderNo = models.CharField(max_length=1, choices=PayType, default="0", unique=True)
    payType = models.CharField(max_length=1, choices=PayType,default="0")
    totalPaid = models.DecimalField(default=1, max_digits=3, decimal_places=0)
    orderTime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name_plural = "6. 订单查看"
    def __str__(self):
        return self.orderNo