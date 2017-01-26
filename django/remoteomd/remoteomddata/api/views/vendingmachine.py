from localomddata.api.serializers.vendingmachine import VendingMachineCUSerializer,VendingMachineDetailSerializer,VendingMachineListSerializer
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
from localomddata.models.vendingmachine import VendingMachine


class VendingMachineCreateAPIView(CreateAPIView):
    queryset =VendingMachine.objects.all()
    serializer_class =VendingMachineCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class VendingMachineDetailAPIView(RetrieveAPIView):
    queryset =VendingMachine.objects.all()
    serializer_class =VendingMachineDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class VendingMachineUpdateAPIView(RetrieveUpdateAPIView):
    queryset =VendingMachine.objects.all()
    serializer_class =VendingMachineCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class VendingMachineDeleteAPIView(DestroyAPIView):
    queryset =VendingMachine.objects.all()
    serializer_class =VendingMachineDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class VendingMachineListAPIView(ListAPIView):
    queryset =VendingMachine.objects.all()
    serializer_class =VendingMachineListSerializer

    #def get_queryset()



