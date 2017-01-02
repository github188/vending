from rest_framework.serializers import ModelSerializer

from cashMachine.models.cashboxlog import CashboxLog
from cashMachine.models.cashboxoperate import CashboxOperate
from cashMachine.models.ordermain import OrderMain


class CashboxOperateSerializer(ModelSerializer):
    class Meta:
        model = CashboxOperate
        fields = ('id', 'operateName', 'operateData', 'createTime')

class CashboxLogSerializer(ModelSerializer):
    class Meta:
        model = CashboxLog
        fields = ('id', 'operate', 'operateStatus','retData', 'createTime')

class OrderMainSerializer(ModelSerializer):
    class Meta:
        model = OrderMain
        fields = ('id', 'slot', 'product','itemCount','payType',  'totalPaid', 'createTime')  #'user', 'status',
