from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from localomddata.models.productcategory import ProductCategory
from localomddata.models.productprovider import ProductProvider


class ProductManager(models.Manager):
    def byName(self, *args, **kwargs):
        return super(ProductManager, self).filter(productName=args[0])
    def byPeriod(self, *args):
        return super(ProductManager, self).filter(orderTime__gte=args[0]).filter(orderTime__lte=args[1])


predicateDict = {
     "Product.provider": "products"
    ,"Product.orderByUser":"orderedProducts"
    ,"Product.category":"products"
    ,"Product.user": "products"

}
class Product(models.Model):
    OrderCountUnit = (
        ("piece", "个"),
        ("package", "包"),
        ("case", "盒"),
        ("kilogram", "公斤"),
        ("batch", "批次"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Product.user"], default=1, verbose_name = "创建人")
    provider = models.ForeignKey(ProductProvider, related_name=predicateDict["Product.provider"], on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "供应商" )
    orderUnitPrice = models.PositiveSmallIntegerField("订购单价", default=90, validators=[MinValueValidator(1), MaxValueValidator(500)]);
    orderTotalPrice = models.PositiveSmallIntegerField("订购总价", validators=[MinValueValidator(1), MaxValueValidator(10000)]);
    orderCount = models.PositiveSmallIntegerField("订购数量", default=1, validators=[MinValueValidator(1), MaxValueValidator(10000)]);
    orderCountUnit = models.CharField("订购单位", max_length=20, choices = OrderCountUnit)
    orderTime = models.DateTimeField("订购时间", auto_now = False, auto_now_add=False)
    orderByUser =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Product.orderByUser"],  default=1, verbose_name = "采购人")
    imageRefUrl = models.URLField("图片参考", null=True)
    imageListUrl = models.URLField("列表图", null=True)
    imageDetailUrl = models.URLField("详情图", null=True)
    isActive = models.BooleanField("生效", default=False)
    productName = models.CharField("名称", max_length=120)
    productSumary = models.CharField("摘要", max_length=500)
    productDesc = models.CharField("详细", max_length=1000)
    saleUnitPrice =  models.PositiveSmallIntegerField("单品售价", default=500, validators=[MinValueValidator(1), MaxValueValidator(500)]);
    productBarUrl = models.URLField("支付条码地址", null=True)
    category = models.ManyToManyField(ProductCategory, related_name=predicateDict["Product.category"], verbose_name= "分类")
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    updateTime = models.DateTimeField("修改时间", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = verbose_name_plural = "5. 商品详细"
    def __str__(self):
        return self.productName

def createProductOrderTotalPrice(instance):
        return instance.orderUnitPrice * instance.orderCount

def pre_save_product_receiver(sender, instance, *args, **kwargs):
        if not instance.orderTotalPrice:
            instance.orderTotalPrice = createProductOrderTotalPrice(instance)

pre_save.connect(pre_save_product_receiver, sender=Product)
