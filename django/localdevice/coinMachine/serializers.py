from rest_framework.serializers import ModelSerializer

from coinMachine.models import CoinChargeLog


class CoinMachineLogSerializer(ModelSerializer):
    class Meta:
        model = CoinChargeLog
        fields = ('id', 'retData', 'createTime')