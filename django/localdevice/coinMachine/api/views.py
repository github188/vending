from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView

from coinMachine.models import CoinChargeLog
from coinMachine.serializers import CoinMachineLogSerializer


class CoinMachineView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CoinChargeLog.objects.all().order_by("-id")[:2]
    serializer_class = CoinMachineLogSerializer

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        response = self.create(request, *args, **kwargs)
        return response

class CoinLogDetailView(RetrieveAPIView):
    queryset = CoinChargeLog.objects.all()
    serializer_class = CoinMachineLogSerializer
    lookup_field = 'id'