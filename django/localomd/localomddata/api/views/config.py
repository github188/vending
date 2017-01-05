from localomddata.api.serializers.config import ConfigCUSerializer, ConfigDetailSerializer, ConfigListSerializer
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
from localomddata.models.config import Config


class ConfigCreateAPIView(CreateAPIView):
    queryset =Config.objects.all()
    serializer_class =ConfigCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ConfigDetailAPIView(RetrieveAPIView):
    queryset =Config.objects.all()
    serializer_class =ConfigDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class ConfigUpdateAPIView(RetrieveUpdateAPIView):
    queryset =Config.objects.all()
    serializer_class =ConfigCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class ConfigDeleteAPIView(DestroyAPIView):
    queryset =Config.objects.all()
    serializer_class =ConfigDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class ConfigListAPIView(ListAPIView):
    serializer_class =ConfigListSerializer

    def get_queryset(self):
        name = self.request.query_params.get('confname', None)
        queryset =Config.objects.all()
        if (name is not None):
            print("now name: " + name);
            queryset = queryset.filter(confname__exact=name)
        return queryset




