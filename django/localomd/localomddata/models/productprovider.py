from django.conf import settings
from django.db import models
predicateDict = {
    "ProductProvider.user": "productprovider",
}
class ProductProvider(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["ProductProvider.user"], default=1, verbose_name = "创建人")

    companyName = models.CharField("公司名", max_length=120, unique=True)
    contactName = models.CharField("联系人名", max_length=120)
    contactTel = models.CharField("联系电话", max_length=11, null = True)
    siteUrl = models.URLField("站点地址", null=True, unique=True)
    class Meta:
        verbose_name = verbose_name_plural = "3. 产品供应"
    def __str__(self):
        return self.companyName