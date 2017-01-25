from django.db import models

"""
  for most common fields
"""
class CommonFields(models.Model):
    #sendFlag is the number(default-1) of tasks for sending.
    # different value mapped by different sync task, unless it's changed to 1.
    sendFlag = models.PositiveSmallIntegerField("发送标志", default=2)
    createTime = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True