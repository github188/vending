
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

from localomddata.api.serializers.coinmachine import CoinChangeLogCUSerializer, CoinChangeLogDetailSerializer, \
    CoinChangeLogListSerializer
from localomddata.models.coinmachine import CoinChangeLog


class CoinChangeCreateAPIView(CreateAPIView):
    queryset =CoinChangeLog.objects.all()
    serializer_class = CoinChangeLogCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CoinChangeDetailAPIView(RetrieveAPIView):
    queryset =CoinChangeLog.objects.all()
    serializer_class =CoinChangeLogDetailSerializer
    lookup_field = 'id'


class CoinChangeUpdateAPIView(RetrieveUpdateAPIView):
    queryset =CoinChangeLog.objects.all()
    serializer_class =CoinChangeLogCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly] #, IsOwnerOrReadOnly
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class CoinChangeDeleteAPIView(DestroyAPIView):
    queryset =CoinChangeLog.objects.all()
    serializer_class =CoinChangeLogDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class CoinChangeListAPIView(ListAPIView):
    serializer_class =CoinChangeLogListSerializer
    queryset = CoinChangeLog.objects.all()




