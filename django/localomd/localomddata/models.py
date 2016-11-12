from django.db import models
from django.conf import settings
# Create your models here.

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
        ("1037F", "1037F")
    )
    ControllerBoardType = (
        ("Banma", "banma")
    )
    MonitorType = (
        ("Antel", "Antel")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    oursmediaSkuNo = models.CharField(max_length=120, unique=True)
    vmType = models.CharField(max_length=20, choices = VmTypeChoice);
    cashBoxType = models.CharField(max_length=20, choices = CashBoxType)
    coinBoxType = models.CharField(max_length=20, choices = CoinBoxType)
    masterBoardType = models.CharField(max_length=20, choices = MasterBoardType)
    controllerBoardType = models.CharField(max_length=20, choices = ControllerBoardType)
    monitorType = models.CharField(max_length=20, choices = MonitorType);
    num_SpringSlot = models.PositiveSmallIntegerField(default=64);
    num_GridSlot = models.PositiveSmallIntegerField(default=0);
    num_Cabinet = models.PositiveSmallIntegerField(default=1);
    charger = models.ForeignKey(settings.AUTH_USER_MODEL, default=1);
    chargerTel = models.CharField(max_length=11);
    installAddress = models.CharField(max_length=240, unique=True);

class slot(models.Model):
    ControllType = (
        ('spring', '弹簧'),
        ('grid', '格子'),
    )
    vmSkuNo = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    slotNo = models.CharField(max_length=120, unique=True)
    capacity = models.PositiveSmallIntegerField(default=1);
    controllType = models.CharField(max_length=20, choices=ControllType)
    currentNum = models.PositiveSmallIntegerField(default=0)
    malfunctionReportCount = models.PositiveSmallIntegerField(default=0)
    product = models.ForeignKey(product, on_delete=models.SET_NULL, blank=True, null=True)

class productprovider(models.Model):
    companyName = models.CharField(max_length=120, unique=True)
    contactName = models.CharField(max_length=120, unique=True)
    contactTel = models.CharField(length=11, null = True)
    siteUrl = models.URLField(null=True)


class product(models.Model):
    OrderCountUnit = (
        ("piece", "个"),
        ("package", "包"),
        ("kilogram", "公斤"),
    )
    provider = models.ForeignKey(productprovider, on_delete=models.SET_NULL, blank=True, null=True )
    orderTotalPrice = models.PositiveSmallIntegerField(default=1000);
    orderCount = models.PositiveSmallIntegerField(default=1);
    orderCountUnit = models.CharField(max_length=20, choices = OrderCountUnit)
    orderTime = models.DateTimeField(auto_now = False, auto_now_add=True)
    orderBy = user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    imageRefUrl = models.URLField(null=True)
    imageListUrl = models.URLField
    imageDetailUrl = models.URLField
    isActive = models.BooleanField(default=False)
    productName = models.CharField(max_length=120, choices = OrderCountUnit)
    productSumary = models.CharField(max_length=500, choices = OrderCountUnit)
    productDesc = models.CharField(max_length=1000, choices = OrderCountUnit)
    productPrice =  models.PositiveSmallIntegerField(default=1000);
    productBarUrl = models.URLField(null=True)
    category = models.ManyToManyField(category, null=True)

class category(models.Model):
    vmSkuNo = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    catName = models.CharField(max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True)

class order_main(models.Model):
    PayType = {
        ("0","cash"),("1","wechat")
    }
    slot = models.ForeignKey(slot, on_delete=models.SET_NULL, blank=True, null=True)
    payType = models.CharField(max_length=1, choices=PayType,default="0")
    totalPaid = models.DecimalField(default=0)
    orderTime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField(auto_now_add=True, auto_now=True)
