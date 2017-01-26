from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models
from rest_framework import authentication
from rest_framework import exceptions

predicateDict = {
    "Login.vmSlug": "logins"
    ,"Login.user": "logins"

}

LoginlogResultType = (
    ('Y', '成功'),
    ('N', '失败'),
)

loginFailCnt = 1


class OMDAuthentication(authentication.BaseAuthentication):
    LOGINFAIL_THRESHOLD = 5
    LOGINFAIL_TIMEWAIT = 10
    def authenticate(self, request):
        if(request.path != '/api/data/api-token-auth/'):
            return
        global loginFailCnt
        username = request.data['username']
        if not username:
            print("no username detected")
            return None
        lastErrLog = Loginlog.objects.filter(loginResult__exact='N').order_by('-id').first()
        if(lastErrLog is not None):
            if lastErrLog.createTime + timedelta(minutes=self.LOGINFAIL_TIMEWAIT) > timezone.now():
                raise exceptions.AuthenticationFailed('帐号已被锁定, 请'+str(self.LOGINFAIL_TIMEWAIT)+'分钟之后再尝试')

        loginLog = Loginlog()
        if (loginFailCnt >= self.LOGINFAIL_THRESHOLD):
            loginLog.username = username
            loginLog.password = request.data['password']
            loginLog.loginResult = 'N'
            loginLog.save()
            loginFailCnt = 0
            raise exceptions.AuthenticationFailed('帐号已被锁定, 请' + str(self.LOGINFAIL_TIMEWAIT) + '分钟之后再尝试')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            loginFailCnt += 1
            raise exceptions.AuthenticationFailed('无效登录,还可以尝试' + str(self.LOGINFAIL_THRESHOLD + 1 - loginFailCnt) + '次')

        credentials = {
            'username': username,
            'password': request.data['password']
        }
        user = authenticate(**credentials)
        if user is None or not user.is_active:
            loginFailCnt += 1
            raise exceptions.AuthenticationFailed('无效登录,还可以尝试' + str(self.LOGINFAIL_THRESHOLD + 1 - loginFailCnt) + '次')

        loginLog.username = username
        loginLog.loginResult = 'Y'
        # loginLog.user = request.user
        loginLog.save()
        loginFailCnt = 0
        return (user, None)


class Loginlog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=predicateDict["Login.user"], default=1, verbose_name = "创建人")
    # vendingMachine = models.ForeignKey(VendingMachine, related_name=predicateDict["Login.vmSlug"], on_delete=models.CASCADE, verbose_name = "售货机编号")
    loginResult = models.CharField("登录结果", max_length=20, choices=LoginlogResultType)
    username = models.CharField("使用用户名", max_length=60, )
    password = models.CharField("使用密码", max_length=60, )
    createTime = models.DateTimeField("发生时间", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = verbose_name_plural = "13. 登录日志"
    def __str__(self):
        return str(self.id)