from rest_framework.serializers import ModelSerializer

from controlBoard.models import ControlBoardInput, ControlBoardOutput


class ControlBoardInSerializer(ModelSerializer):
    class Meta:
        model = ControlBoardInput
        fields = ('id', 'slotNo', 'inputDesc', 'turnCnt', 'createTime')

class ControlBoardOutSerializer(ModelSerializer):
    class Meta:
        model = ControlBoardOutput
        fields = ('id', 'input', 'outputDesc', 'createTime')