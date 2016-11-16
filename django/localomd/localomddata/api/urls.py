from django.conf.urls import url
from django.contrib import admin


from .views import (
    MoneyChargeListAPIView, MoneyChargeCreateAPIView, MoneyChargeDetailAPIView, MoneyChargeUpdateAPIView,
    MoneyChargeDeleteAPIView)

urlpatterns = [
    url(r'^moneycharge/$', MoneyChargeListAPIView.as_view(), name='moneycharge'),
    url(r'^moneycharge/create/$', MoneyChargeCreateAPIView.as_view(), name='moneycharge-create'),
    url(r'^moneycharge/(?P<slug>[\w-]+)/$', MoneyChargeDetailAPIView.as_view(), name='moneycharge-detail'),
    url(r'^moneycharge/(?P<slug>[\w-]+)/edit/$', MoneyChargeUpdateAPIView.as_view(), name='moneycharge-update'),
    url(r'^moneycharge/(?P<slug>[\w-]+)/delete/$', MoneyChargeDeleteAPIView.as_view(), name='moneycharge-delete'),
]
