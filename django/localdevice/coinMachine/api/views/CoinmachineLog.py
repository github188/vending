from rest_framework.generics import RetrieveAPIView, ListAPIView

from coinMachine.models import CoinMachineOutput
from controlBoard.api.serializers import ControlBoardOutSerializer
from controlBoard.models import ControlBoardOutput

class CoinMachineOutputLogDetailView(RetrieveAPIView):
    queryset = ControlBoardOutput.objects.all()
    serializer_class = ControlBoardOutSerializer
    lookup_field = 'id'

class CoinMachineOutputView(ListAPIView):
    serializer_class = ControlBoardOutSerializer
    def get_queryset(self):
        queryset = CoinMachineOutput.objects.all().order_by("-id")
        inputId = self.request.query_params.get('inputId', None)
        if (inputId is not None):
            print("now InputId: " + inputId);
            queryset = queryset.filter(input__exact=inputId)
        return queryset
