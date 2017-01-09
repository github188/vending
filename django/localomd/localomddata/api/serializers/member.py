from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from localomddata.models.member import Member


class MemberSerializer(Serializer):
    pass

class MemberCUSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'owner', 'user', 'balance',)


class MemberListSerializer(ModelSerializer):
    #www.django-rest-framework.org/api-guide/fields/#source
    #stackoverflow.com/questions/27851138/how-can-i-get-the-parent-object-in-django-rest-framework-serializer
    #stackoverflow.com/questions/18396547/django-rest-framework-adding-additional-field-to-modelserializer
    #www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    date_joined = serializers.DateTimeField(read_only=True, source = "user.date_joined")
    username = serializers.CharField(read_only=True, source = "user.username")
    class Meta:
        model = Member
        fields = MemberCUSerializer.Meta.fields + ('date_joined','username')

class MemberDetailSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('id',) + MemberCUSerializer.Meta.fields
