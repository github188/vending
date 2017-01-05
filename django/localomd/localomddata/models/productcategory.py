from django.conf import settings
from django.db import models

predicateDict = {
    "ProductCategory.parent": "children", "ProductCategory.user": "productcategory",
}

class ProductCategory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["ProductCategory.user"], default=1, verbose_name = "创建人")

    catName = models.CharField("分类名", max_length=20)
    slug = models.CharField("编辑名", max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True, related_name=predicateDict["ProductCategory.parent"], verbose_name = "父类")
    class Meta:
        verbose_name = verbose_name_plural = "04. 商品类别"
    def __str__(self):
        return self.catName
#########################################################################################################
