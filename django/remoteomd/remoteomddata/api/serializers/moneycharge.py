from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.moneycharge import MoneyCharge


class MoneyChargeSerializer(Serializer):
    pass

class MoneyChargeCUSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = ('id', 'vmSlug', 'cashAmount', 'coinAmount',)


class MoneyChargeListSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = MoneyChargeCUSerializer.Meta.fields + ('createTime', 'updateTime')

class MoneyChargeDetailSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = MoneyChargeCUSerializer.Meta.fields






""""

from posts.models import Post
from posts.api.serializers import PostDetailSerializer


data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",
    
}

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""