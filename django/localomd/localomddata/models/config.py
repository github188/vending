from django.conf import settings
from django.db import models

from localomddata.models.vendingmachine import VendingMachine

predicateDict = {
    "Config.vmSlug": "configs"
    ,"Config.user": "configs"

}
class Config(models.Model):
    ConfigType = (
        ('COM', '设备端口'),
        ('url', 'API地址'),
        ('locallib','本地库路径')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Config.user"], default=1, verbose_name = "创建人")
    vendingMachine = models.ForeignKey(VendingMachine, related_name=predicateDict["Config.vmSlug"], on_delete=models.CASCADE, verbose_name = "售货机编号")
    configType = models.CharField("配置类型", max_length=20, choices=ConfigType)
    confname = models.CharField("配置名称", max_length=60, unique=True)
    confvalue = models.CharField("配置值", max_length=60, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = "10. 配置详细"
    def __str__(self):
        return str(self.id)