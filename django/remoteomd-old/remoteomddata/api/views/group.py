from django.contrib.auth.models import Group
from remoteomddata.api.serializers.group import GroupCUSerializer, GroupDetailSerializer, GroupListSerializer
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from remoteomddata.api.permissions import IsOwnerOrReadOnly


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class GroupDetailAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class GroupUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class GroupDeleteAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer

    #def get_queryset()



