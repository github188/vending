from remoteomddata.api.serializers.ordermain import OrderMainCUSerializer, OrderMainDetailSerializer, OrderMainListSerializer
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
from remoteomddata.models.ordermain import OrderMain


class OrderMainCreateAPIView(CreateAPIView):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OrderMainDetailAPIView(RetrieveAPIView):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class OrderMainUpdateAPIView(RetrieveUpdateAPIView):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class OrderMainDeleteAPIView(DestroyAPIView):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class OrderMainListAPIView(ListAPIView):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainListSerializer

    #def get_queryset()



