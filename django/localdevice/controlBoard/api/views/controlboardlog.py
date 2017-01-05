from rest_framework.generics import RetrieveAPIView, ListAPIView

from controlBoard.api.serializers import ControlBoardOutSerializer
from controlBoard.models import ControlBoardOutput


class ControlboardLogDetailView(RetrieveAPIView):
    queryset = ControlBoardOutput.objects.all()
    serializer_class = ControlBoardOutSerializer
    lookup_field = 'id'

class ControlboardLogListView(ListAPIView):
    serializer_class = ControlBoardOutSerializer
    def get_queryset(self):
        queryset = ControlBoardOutput.objects.all().order_by("-id")
        inputId = self.request.query_params.get('inputId', None)
        if (inputId is not None):
            print("now InputId: " + inputId);
            queryset = queryset.filter(input__exact=inputId)
        return queryset