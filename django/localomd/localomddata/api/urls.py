from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet, GroupViewSet
from .views import (
    MoneyChargeListAPIView, MoneyChargeCreateAPIView, MoneyChargeDetailAPIView, MoneyChargeUpdateAPIView,
    MoneyChargeDeleteAPIView)

router = DefaultRouter()
router.register(r'^users', UserViewSet)
router.register(r'^groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^moneycharge/$', MoneyChargeListAPIView.as_view(), name='moneycharge'),
    url(r'^moneycharge/create/$', MoneyChargeCreateAPIView.as_view(), name='moneycharge-create'),
    url(r'^moneycharge/(?P<id>[\w-]+)/$', MoneyChargeDetailAPIView.as_view(), name='moneycharge-detail'),
    url(r'^moneycharge/(?P<id>[\w-]+)/edit/$', MoneyChargeUpdateAPIView.as_view(), name='moneycharge-update'),
    url(r'^moneycharge/(?P<id>[\w-]+)/delete/$', MoneyChargeDeleteAPIView.as_view(), name='moneycharge-delete'),
]
