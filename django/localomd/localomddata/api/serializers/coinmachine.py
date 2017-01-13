from rest_framework.serializers import ModelSerializer, Serializer

from localomddata.models.coinmachine import CoinChangeLog


class CoinChangeLogSerializer(ModelSerializer):
    pass

class CoinChangeLogCUSerializer(ModelSerializer):
    class Meta:
        model = CoinChangeLog
        fields = ("amountBefore", "amountData")


class CoinChangeLogListSerializer(ModelSerializer):
    class Meta:
        model = CoinChangeLog
        fields = ('id', 'user',) + CoinChangeLogCUSerializer.Meta.fields + ("amountAfter", 'createTime',)

class CoinChangeLogDetailSerializer(ModelSerializer):
    class Meta:
        model = CoinChangeLog
        fields = CoinChangeLogListSerializer.Meta.fields