from rest_framework.serializers import ModelSerializer

from coinMachine.models import CoinMachineInput, CoinMachineOutput


class CoinMachineInSerializer(ModelSerializer):
    class Meta:
        model = CoinMachineInput
        fields = ('id', 'payoutCnt', 'inputDesc', 'createTime')

class CoinMachineOutSerializer(ModelSerializer):
    class Meta:
        model = CoinMachineOutput
        fields = ('id', 'input', 'outputDesc', 'createTime')