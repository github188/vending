from localomddata.api.serializers.productprovider import ProductProviderCUSerializer,ProductProviderDetailSerializer,ProductProviderListSerializer
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
from localomddata.models.productprovider import ProductProvider


class ProductProviderCreateAPIView(CreateAPIView):
    queryset =ProductProvider.objects.all()
    serializer_class =ProductProviderCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProductProviderDetailAPIView(RetrieveAPIView):
    queryset =ProductProvider.objects.all()
    serializer_class =ProductProviderDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class ProductProviderUpdateAPIView(RetrieveUpdateAPIView):
    queryset =ProductProvider.objects.all()
    serializer_class =ProductProviderCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class ProductProviderDeleteAPIView(DestroyAPIView):
    queryset =ProductProvider.objects.all()
    serializer_class =ProductProviderDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class ProductProviderListAPIView(ListAPIView):
    queryset =ProductProvider.objects.all()
    serializer_class =ProductProviderListSerializer

    #def get_queryset()



