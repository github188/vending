from django.db import models

class CommonManager(models.Manager):
    def get_querySet(self):
        return super(CommonManager, self).get_queryset().filter(self.isDeleted == 'False')

class UnSyncedManager(models.Manager):
    def get_querySet(self):
        return super(CommonManager, self).get_queryset().filter(self.isDeleted == 'False').filter(self.sendFlag > '1')
"""
  for most common fields
"""
class CommonFields(models.Model):
    #sendFlag is the num of binary, each bit is a system, for sending.
    # different value mapped by different sync task, unless it's changed to 1.
    sendFlag = models.PositiveSmallIntegerField("发送标志", default=2)
    isDeleted = models.BooleanField("已删除标记", default=False)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    updateTime = models.DateTimeField("修改时间", auto_now_add=False, auto_now=True)  #, null=True

    objects = models.Manager()
    valid_objects = CommonManager()
    unsynced_objects = UnSyncedManager()

    class Meta:
        abstract = True