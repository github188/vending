from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from remoteomddata.models.productcategory import ProductCategory


class ProductCategorySerializer(Serializer):
    pass

class ProductCategoryCUSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('catName', 'slug', 'parent',)


class ProductCategoryListSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ProductCategoryCUSerializer.Meta.fields

class ProductCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id',) + ProductCategoryCUSerializer.Meta.fields

