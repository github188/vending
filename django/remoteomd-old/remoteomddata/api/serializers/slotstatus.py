from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from remoteomddata.models.slot import Slot
from remoteomddata.models.slotstatus import SlotStatus


class SlotStatusSerializer(Serializer):
    pass

class SlotStatusCUSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = ('slot','product', 'currentItemNum', 'malfunctionReportCount')


class SlotStatusListSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = SlotStatusCUSerializer.Meta.fields + ('createTime', 'updateTime')

class SlotStatusDetailSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = ('id',) + SlotStatusCUSerializer.Meta.fields
