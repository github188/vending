from django.conf.urls import url

from coinMachine.api.views.CoinmachineInput import CoinMachineInputView
from coinMachine.api.views.CoinmachineLog import CoinMachineOutputView, CoinMachineOutputLogDetailView

urlpatterns = [
    url(r'^run/$', CoinMachineInputView.as_view(), name='run'),
    # url(r'^coinlog/', CoinMachineLogView.as_view(), name='coinMachine-log'),
    url(r'^coinoutputlog/', CoinMachineOutputView.as_view(), name='coinMachine-outputlog-list'),
    url(r'^coinoutputlog/(?P<id>[\w-]+)/$', CoinMachineOutputLogDetailView.as_view(), name='coinMachine-outputlog-detail'),
]
