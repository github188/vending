
from rest_framework.generics import RetrieveAPIView, ListAPIView

from cashMachine.api.serializers import CashboxLogSerializer
from cashMachine.models.cashboxlog import CashboxLog


class CashBoxLogView(ListAPIView):
    serializer_class = CashboxLogSerializer
    def get_queryset(self):
        queryset = CashboxLog.objects.all().order_by("-id")
        operateName = self.request.query_params.get('operateName', None)
        if (operateName is not None):
            print("now operateName: " + operateName);
            queryset = queryset.filter(operate__operateName__exact=operateName)
        operate = self.request.query_params.get('operate', None)
        if (operate is not None):
            print("now operate: " + operate);
            queryset = queryset.filter(operate__exact=operate)
        limit = self.request.query_params.get('limit', '50')
        queryset = queryset[:int(limit)]
        return queryset

class CashBoxLogByOperateView(ListAPIView):
    serializer_class = CashboxLogSerializer
    def get_queryset(self):
        operate = self.kwargs['operate']
        queryset = CashboxLog.objects.filter(operate__operateName__exact=operate).order_by("-id")
        limit = self.request.query_params.get('limit', '50')
        queryset = queryset[:int(limit)]
        return queryset



class CashBoxLogDetailView(RetrieveAPIView):
    queryset = CashboxLog.objects.all()
    serializer_class = CashboxLogSerializer
    lookup_field = 'id'
