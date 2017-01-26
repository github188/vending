from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-user


class Member(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ownedmembers", default=1, verbose_name = "创建人")
    user = models.OneToOneField(User, related_name="member", on_delete=models.CASCADE)
    balance = models.PositiveSmallIntegerField(default=0,)
    telNo = models.CharField(max_length=11, null=True)
    wechatNo = models.CharField(max_length=11, null=True)
    website = models.URLField(null=True)
    class Meta:
        verbose_name = verbose_name_plural = "11. 会员"
    def __str__(self):
        return str(self.id)
