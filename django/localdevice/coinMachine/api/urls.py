from django.conf.urls import url

from coinMachine.api.views import CoinMachineView, CoinLogDetailView

urlpatterns = [
    url(r'^coinlog/', CoinMachineView.as_view(), name='coinMachine-list'),
    url(r'^coindetail/$', CoinLogDetailView.as_view(), name='coinMachine-detail'),

]
