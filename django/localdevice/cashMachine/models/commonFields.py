from django.db import models


class UnSyncedManager(models.Manager):
    def get_querySet(self):
        return super(UnSyncedManager, self).get_queryset().filter(self.sendFlag > '1')
"""
  for most common fields
"""
class CommonFields(models.Model):
    #sendFlag is the num of binary, each bit is a system, for sending.
    # different value mapped by different sync task, unless it's changed to 1.
    sendFlag = models.PositiveSmallIntegerField("发送标志", default=2)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)

    objects = models.Manager()
    unsynced_objects = UnSyncedManager()

    class Meta:
        abstract = True