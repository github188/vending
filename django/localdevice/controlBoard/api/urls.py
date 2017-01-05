from django.conf.urls import url

from controlBoard.api.views.ControlBoardInput import ControlBoardInputView
from controlBoard.api.views.controlboardlog import ControlboardLogDetailView, ControlboardLogListView

urlpatterns = [
    url(r'^testrun/$', ControlBoardInputView.as_view(), name='testrun'),
    # url(r'^input/$', ControlBoardInputView.as_view(), name='testrun'),
    url(r'^output/$', ControlboardLogDetailView.as_view(), name='outlog'),
    url(r'^outputlist/$', ControlboardLogListView.as_view(), name='outloglist'),
]
