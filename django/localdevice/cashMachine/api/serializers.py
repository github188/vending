from rest_framework.serializers import ModelSerializer

from cashMachine.models import CashboxOperate, CashboxLog


class CashboxOperateSerializer(ModelSerializer):
    class Meta:
        model = CashboxOperate
        fields = ('id', 'operateName', 'operateData', 'createTime')

class CashboxLogSerializer(ModelSerializer):
    class Meta:
        model = CashboxLog
        fields = ('id', 'operate', 'operateStatus','retData', 'createTime')