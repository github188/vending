from django.contrib.auth.decorators import login_required
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
from localomddata.api.serializers.moneycharge import MoneyChargeCUSerializer, MoneyChargeDetailSerializer, \
    MoneyChargeListSerializer
from localomddata.models import MoneyCharge



class MoneyChargeCreateAPIView(CreateAPIView):
    queryset = MoneyCharge.objects.all()
    serializer_class = MoneyChargeCUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MoneyChargeDetailAPIView(RetrieveAPIView):
    queryset = MoneyCharge.objects.all()
    serializer_class = MoneyChargeDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"


class MoneyChargeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = MoneyCharge.objects.all()
    serializer_class = MoneyChargeCUSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class MoneyChargeDeleteAPIView(DestroyAPIView):
    queryset = MoneyCharge.objects.all()
    serializer_class = MoneyChargeDetailSerializer
    lookup_field = 'id'
    #lookup_url_kwarg = "abc"

class MoneyChargeListAPIView(ListAPIView):
    queryset = MoneyCharge.objects.all()
    print(queryset.count())
    serializer_class = MoneyChargeListSerializer

    #def get_queryset()



