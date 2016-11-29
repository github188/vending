from django.conf.urls import url

from controlBoard.api.views import ControlBoardInputView

urlpatterns = [
    url(r'^testrun/$', ControlBoardInputView.as_view(), name='testrun'),

]
