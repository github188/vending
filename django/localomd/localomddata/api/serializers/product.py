from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.product import Product

class ProductSerializer(Serializer):
    pass

class ProductCUSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('provider', 'orderUnitPrice', 'orderCount','orderCountUnit'
                  ,'orderTime','orderByUser','imageRefUrl','imageListUrl', 'imageDetailUrl'
                  , 'isActive', 'productName',"productSumary","productDesc","saleUnitPrice"
                  ,"productBarUrl","category"
                  ,)


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ProductCUSerializer.Meta.fields + ('createTime','updateTime',)

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',) + ProductCUSerializer.Meta.fields
