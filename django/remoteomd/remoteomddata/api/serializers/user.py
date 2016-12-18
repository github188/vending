from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer


class UserSerializer(Serializer):
    pass

class UserCUSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff',)


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = UserCUSerializer.Meta.fields + ('date_joined',)

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',) + UserListSerializer.Meta.fields
