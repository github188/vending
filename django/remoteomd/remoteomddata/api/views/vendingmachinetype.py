from localomddata.api.serializers.vendingmachinetype import VendingMachineTypeCUSerializer,VendingMachineTypeDetailSerializer,VendingMachineTypeListSerializer
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
from localomddata.models.vendingmachinetype import VendingMachineType


class VendingMachineTypeCreateAPIView(CreateAPIView):
    queryset =VendingMachineType.objects.all()
    serializer_class =VendingMachineTypeCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class VendingMachineTypeDetailAPIView(RetrieveAPIView):
    queryset =VendingMachineType.objects.all()
    serializer_class =VendingMachineTypeDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class VendingMachineTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset =VendingMachineType.objects.all()
    serializer_class =VendingMachineTypeCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class VendingMachineTypeDeleteAPIView(DestroyAPIView):
    queryset =VendingMachineType.objects.all()
    serializer_class =VendingMachineTypeDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class VendingMachineTypeListAPIView(ListAPIView):
    queryset =VendingMachineType.objects.all()
    serializer_class =VendingMachineTypeListSerializer

    #def get_queryset()



