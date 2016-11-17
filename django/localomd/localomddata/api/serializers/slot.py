from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.slot import Slot

class SlotSerializer(Serializer):
    pass

class SlotCUSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = ('vendingMachine', 'slotNo', 'capacity','controllType', )


class SlotListSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = SlotCUSerializer.Meta.fields

class SlotDetailSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id',) + SlotCUSerializer.Meta.fields
