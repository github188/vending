from rest_framework.serializers import ModelSerializer, Serializer

from localomddata.models.ordermain import OrderMain


class OrderMainSerializer(Serializer):
    pass

class OrderMainCUSerializer(ModelSerializer):
    class Meta:
        model = OrderMain
        fields = ('slot', 'payType','product', 'status', 'itemCount', 'updateTime')


class OrderMainListSerializer(ModelSerializer):
    class Meta:
        model = OrderMain
        fields = OrderMainCUSerializer.Meta.fields + ('createTime',)

class OrderMainDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderMain
        fields = ('id',) + OrderMainCUSerializer.Meta.fields
