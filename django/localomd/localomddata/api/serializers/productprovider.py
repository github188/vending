from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.productprovider import ProductProvider

class ProductProviderSerializer(Serializer):
    pass

class ProductProviderCUSerializer(ModelSerializer):
    class Meta:
        model = ProductProvider
        fields = ('companyName', 'contactName', 'contactTel','siteUrl',)


class ProductProviderListSerializer(ModelSerializer):
    class Meta:
        model = ProductProvider
        fields = ProductProviderCUSerializer.Meta.fields

class ProductProviderDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductProvider
        fields = ('id',) + ProductProviderCUSerializer.Meta.fields
