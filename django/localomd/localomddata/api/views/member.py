from django.contrib.auth.models import User

from localomddata.api.serializers.member import MemberCUSerializer, MemberDetailSerializer, MemberListSerializer
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
from localomddata.models.member import Member


class MemberCreateAPIView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCUSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    def perform_create(self, serializer):
        serializer.save()


class MemberDetailAPIView(RetrieveAPIView):
    queryset =Member.objects.all()
    serializer_class =MemberDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class MemberUpdateAPIView(RetrieveUpdateAPIView):
    queryset =Member.objects.all()
    serializer_class =MemberCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class MemberDeleteAPIView(DestroyAPIView):
    queryset =Member.objects.all()
    serializer_class =MemberDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class MemberListAPIView(ListAPIView):
    serializer_class = MemberListSerializer
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Member.objects.all().order_by("-id")
        username = self.request.query_params.get('username', None)
        if (username is not None):
            print("now operateName: " + username);
            queryset = queryset.filter(user__username__exact=username)
        isManager = self.request.query_params.get('isManager', None)
        if(isManager is not None):
            queryset = queryset.filter(owner=1)
        queryset = queryset[:int(1)]
        return queryset



