from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from localomddata.models.productcategory import ProductCategory
from localomddata.models.vendingmachinetype import VendingMachineType

predicateDict = {
    "VendingMachineType.user": "createdmachines"
    ,"VendingMachine.charger": "chargingmachines"
    , "VendingMachine.vmType": "machines"
    , "VendingMachine.productCategory": "machines"
    , "VendingMachine.user": "machines"
}
class VendingMachine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["VendingMachine.user"], default=1, verbose_name = "创建人")

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
        slug = "%s%s" %(slugPrefix, '{:03d}'.format(qs.first().id+1))
    else:
        slug=slugPrefix + '{:03d}'.format(1)
    return slug

def pre_save_vm_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = createVmSlug(instance)

pre_save.connect(pre_save_vm_receiver, sender=VendingMachine)