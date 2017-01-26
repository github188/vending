from localomddata.api.serializers.productcategory import ProductCategoryCUSerializer, ProductCategoryDetailSerializer, ProductCategoryListSerializer
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
from localomddata.models.productcategory import ProductCategory


class ProductCategoryCreateAPIView(CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProductCategoryDetailAPIView(RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class ProductCategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class ProductCategoryDeleteAPIView(DestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryListSerializer

    #def get_queryset()



