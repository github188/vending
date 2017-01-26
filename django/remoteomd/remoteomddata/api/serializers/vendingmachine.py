from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.vendingmachine import VendingMachine

"""
    slug = models.CharField("编号", max_length=120, unique=True)
    vmType = models.ForeignKey(VendingMachineType, verbose_name="售货机类型", related_name=predicateDict['VendingMachine.vmType'])
    charger = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name=predicateDict["VendingMachine.charger"], verbose_name = "负责人");
    productCategory = models.ManyToManyField(ProductCategory, related_name=predicateDict["VendingMachine.productCategory"], verbose_name="商品分类")
    chargerTel = models.CharField("联系电话", max_length=11);
    installAddress = models.CharField("安装地址", max_length=240, unique=True);
    installTime = models.DateTimeField("安装时间", auto_now_add=False, auto_now=False)
    aliveTime = models.DateTimeField("运行开始时间", auto_now_add=False, auto_now=False)
"""

class VendingMachineSerializer(Serializer):
    pass

class VendingMachineCUSerializer(ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ('vmType', 'charger', 'productCategory', 'chargerTel', 'installAddress', 'installTime', 'aliveTime',)


class VendingMachineListSerializer(ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ('slug',) + VendingMachineCUSerializer.Meta.fields

class VendingMachineDetailSerializer(ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ('id',) + VendingMachineListSerializer.Meta.fields
