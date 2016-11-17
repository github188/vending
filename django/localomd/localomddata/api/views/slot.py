from localomddata.api.serializers.slot import SlotCUSerializer,SlotDetailSerializer,SlotListSerializer
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
from localomddata.models.slot import Slot


class SlotCreateAPIView(CreateAPIView):
    queryset =Slot.objects.all()
    serializer_class =SlotCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class SlotDetailAPIView(RetrieveAPIView):
    queryset =Slot.objects.all()
    serializer_class =SlotDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class SlotUpdateAPIView(RetrieveUpdateAPIView):
    queryset =Slot.objects.all()
    serializer_class =SlotCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class SlotDeleteAPIView(DestroyAPIView):
    queryset =Slot.objects.all()
    serializer_class =SlotDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class SlotListAPIView(ListAPIView):
    queryset =Slot.objects.all()
    serializer_class =SlotListSerializer

    #def get_queryset()



