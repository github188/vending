from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# class JsonApiFields:
#     imageUrl = models.CharField(max_length=64)
#     videoUrl = models.CharField(max_length=64)
#     attributesUrl = models.CharField(max_length=64)
#     merNavCategoryUrl =  models.CharField(max_length=64)
#     memberRole = models.CharField(max_length=64)
#     contactMethod = models.CharField;

# docs.djangoproject.com/en/dev/topics/db/models/#meta-options
# docs.djangoproject.com/en/dev/topics/db/queries/#backwards-related-objects

#paytype, category,
class EnumValue(models.Model):
    name = models.CharField()
    type = models.CharField()

class CommonTime(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True
        get_latest_by = ['created']  #default field to use in model Manager's latest() earliest() method
        ordering = ['-created','-updated'] # -descendingOrder ?randomOrder defaultAscendingOrder

class CommonFields(CommonTime):
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    jsonApiUrl = models.URLField()
    desc = models.TextField()

    class Meta(CommonTime.Meta):
        abstract = True
        ordering = ['createdBy','?updatedBy'] # -descendingOrder ?randomOrder defaultAscendingOrder

class Member(models.Model):
    telNo = models.CharField(max_length=16)
    balance = models.IntegerField(default=0)
    creditPoint = models.IntegerField(default=0)
    authUser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)


class MemberRole(models.Model):
    name = models.CharField(max_length=16)
    # authGroup = models.ForeignKey(settings.AUTH_GROUP_MODEL, default=1)

class Term(CommonFields):
    termNo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, max_length=96)
    owner = models.ForeignKey(Member, related_name="owner", default=1)
    manager = models.ForeignKey(Member, related_name="manager", default=1)

class Merchandise(CommonFields):
    name = models.CharField(max_length=140)
    merNo = models.CharField(max_length=64)
    price = models.PositiveSmallIntegerField(default=0)

    class Meta(CommonFields.Meta):
        ordering = ['price']

class Order(CommonTime):
    created = models.DateTimeField(auto_now=True)
    payType = models.ForeignKey(EnumValue, default=1)
    term = models.ForeignKey(Term, default=1)
    totalPrice = models.PositiveSmallIntegerField(default=0)
    paid = models.PositiveSmallIntegerField(default=0)
    wechat = models.CharField(max_length=64)

class OrderLine(CommonTime):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    unitPrice = models.PositiveSmallIntegerField(default=0)
    itemCount = models.PositiveSmallIntegerField(default=0)
    merchandise = models.ForeignKey(Merchandise)

class TermMerRel(CommonFields):
    terminal = models.ForeignKey(Term, on_delete=models.CASCADE)
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    slot = models.PositiveSmallIntegerField(default=0)
    itemCount = models.PositiveSmallIntegerField(default=0)

    # https://docs.djangoproject.com/en/1.10/ref/models/fields/ # django.db.models.DateTimeField
    # https://docs.djangoproject.com/en/1.10/topics/db/models/
    # https://docs.djangoproject.com/en/1.10/intro/overview/#design-your-model