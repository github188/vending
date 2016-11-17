from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

class GroupSerializer(Serializer):
    pass

class GroupCUSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = fields = ('url', 'name')


class GroupListSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = GroupCUSerializer.Meta.fields

class GroupDetailSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id',) + GroupCUSerializer.Meta.fields
