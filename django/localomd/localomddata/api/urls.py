from django.conf.urls import url, include

from localomddata.api.views.moneycharge import MoneyChargeListAPIView, MoneyChargeCreateAPIView, \
    MoneyChargeDetailAPIView, MoneyChargeUpdateAPIView, MoneyChargeDeleteAPIView

urlpatterns = [
    url(r'^moneycharge/$', MoneyChargeListAPIView.as_view(), name='moneycharge'),
    url(r'^moneycharge/create/$', MoneyChargeCreateAPIView.as_view(), name='moneycharge-create'),
    url(r'^moneycharge/(?P<id>[\w-]+)/$', MoneyChargeDetailAPIView.as_view(), name='moneycharge-detail'),
    url(r'^moneycharge/(?P<id>[\w-]+)/edit/$', MoneyChargeUpdateAPIView.as_view(), name='moneycharge-update'),
    url(r'^moneycharge/(?P<id>[\w-]+)/delete/$', MoneyChargeDeleteAPIView.as_view(), name='moneycharge-delete'),
]
