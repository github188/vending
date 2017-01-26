from django.contrib.auth.models import User
from localomddata.api.serializers.user import UserCUSerializer,UserDetailSerializer,UserListSerializer
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

from localomddata.api.permissions import IsOwnerOrReadOnly


class UserCreateAPIView(CreateAPIView):
    queryset =User.objects.all()
    serializer_class =UserCUSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class UserDetailAPIView(RetrieveAPIView):
    queryset =User.objects.all()
    serializer_class =UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset =User.objects.all()
    serializer_class =UserCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class UserDeleteAPIView(DestroyAPIView):
    queryset =User.objects.all()
    serializer_class =UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class UserListAPIView(ListAPIView):
    queryset =User.objects.all()
    serializer_class =UserListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    #def get_queryset()



