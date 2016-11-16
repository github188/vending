from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models import MoneyCharge, VendingMachine, ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['vmSku','catName','slug','parent']

"""
{'vmSku': 1, 'parent': None, 'slug': 'infant', 'catName': '母婴'}


"""
class MoneyChargeSerializer(Serializer):
    pass

class MoneyChargeCUSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = ['vmSku', 'cashAmount', 'coinAmount' ]

class MoneyChargeListSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = MoneyChargeCUSerializer.Meta.fields + [
            'createTime',
            'updateTime'
        ]
class MoneyChargeDetailSerializer(ModelSerializer):
    class Meta:
        model = MoneyCharge
        fields = ['id'] + MoneyChargeCUSerializer.Meta.fields






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