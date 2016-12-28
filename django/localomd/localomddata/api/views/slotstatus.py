from localomddata.api.serializers.slotstatus import SlotStatusCUSerializer, SlotStatusDetailSerializer, SlotStatusListSerializer
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
from localomddata.models.slotstatus import SlotStatus


class SlotStatusCreateAPIView(CreateAPIView):
    queryset =SlotStatus.objects.all()
    serializer_class =SlotStatusCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class SlotStatusDetailAPIView(RetrieveAPIView):
    queryset =SlotStatus.objects.all()
    serializer_class =SlotStatusDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class SlotStatusUpdateAPIView(RetrieveUpdateAPIView):
    queryset =SlotStatus.objects.all()
    serializer_class =SlotStatusCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class SlotStatusDeleteAPIView(DestroyAPIView):
    queryset =SlotStatus.objects.all()
    serializer_class =SlotStatusDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class SlotStatusListAPIView(ListAPIView):
    serializer_class =SlotStatusListSerializer
    queryset = SlotStatus.objects.all()
    # def get_queryset(self):
    #     qs1 = SlotStatus.objects.all()
    #     return qs1



