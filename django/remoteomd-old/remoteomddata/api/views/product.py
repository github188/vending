from remoteomddata.api.serializers.product import ProductCUSerializer,ProductDetailSerializer,ProductListSerializer
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
from remoteomddata.models.product import Product


class ProductCreateAPIView(CreateAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProductDetailAPIView(RetrieveAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class ProductDeleteAPIView(DestroyAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class ProductListAPIView(ListAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductListSerializer

    #def get_queryset()



