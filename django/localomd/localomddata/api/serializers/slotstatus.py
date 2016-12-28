from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.slot import Slot
from localomddata.models.slotstatus import SlotStatus


class SlotStatusSerializer(Serializer):
    pass

class SlotStatusCUSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = ('slot','product','runningStatus', 'currentItemNum', 'malfunctionReportCount')


class SlotStatusListSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = SlotStatusCUSerializer.Meta.fields + ('user', 'createTime', 'updateTime')

class SlotStatusDetailSerializer(ModelSerializer):
    class Meta:
        model = SlotStatus
        fields = ('id',) + SlotStatusCUSerializer.Meta.fields
