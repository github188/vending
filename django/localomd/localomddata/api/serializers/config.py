from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.config import Config
from localomddata.models.slot import Slot

class ConfigCUSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = ('configType', 'confname','confvalue', )


class ConfigListSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = ConfigCUSerializer.Meta.fields

class ConfigDetailSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id',) + ConfigCUSerializer.Meta.fields
