
from threading import Thread

from pip._vendor import requests
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView

from cashMachine.api.serializers import OrderMainSerializer
from cashMachine.models.ordermain import OrderMain


class OperateControlBoard(Thread):
    def __init__(self, requestData):
        Thread.__init__(self)
        self.requestData = {'slotNo':9, 'turnCnt': requestData['itemCount']}
        # self.requestData = {'slotNo': requestData['slot'], 'turnCnt': requestData['itemCount']}

    def run(self):
        print(self.requestData)
        # config = requests.get("http://172.18.0.4/api/data/config/?confname=runcontrolboard")
        # print(config)
        response = requests.post('http://localhost:8000/api/data/controlboard/testrun/',self.requestData)
        print(response);

class OrderMainDetailView(RetrieveAPIView):
    queryset = OrderMain.objects.all();
    serializer_class = OrderMainSerializer
    lookup_field = 'id'

class OrderMainView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = OrderMain.objects.all().order_by("-id")[:50];
    serializer_class = OrderMainSerializer
    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        operateControlBoard = OperateControlBoard(request.data)
        operateControlBoard.setDaemon(True)
        operateControlBoard.start()
        response = self.create(request, *args, **kwargs)
        print(response.data['id'])
        return response