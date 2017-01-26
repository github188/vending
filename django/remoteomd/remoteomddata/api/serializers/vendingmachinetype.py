from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.vendingmachinetype import VendingMachineType


class VendingMachineTypeSerializer(Serializer):
    pass

class VendingMachineTypeCUSerializer(ModelSerializer):
    class Meta:
        model = VendingMachineType
        fields = ('user', 'deliveryType', 'cashBoxType','coinBoxType', 'masterBoardType',
                  'controllerBoardType', 'monitorType', 'num_SpringSlot', 'num_GridSlot', 'num_Cabinet')


class VendingMachineTypeListSerializer(ModelSerializer):
    class Meta:
        model = VendingMachineType
        fields = VendingMachineTypeCUSerializer.Meta.fields

class VendingMachineTypeDetailSerializer(ModelSerializer):
    class Meta:
        model = VendingMachineType
        fields = ('id',) + VendingMachineTypeCUSerializer.Meta.fields
