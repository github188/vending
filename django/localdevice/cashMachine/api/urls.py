from django.conf.urls import url

from cashMachine.api.views.cashboxinput import CashBoxInputView, CashBoxInputDetailView
from cashMachine.api.views.cashboxlog import CashBoxLogView, CashBoxLogDetailView, CashBoxLogByOperateView
from cashMachine.api.views.ordermainser import OrderMainView, OrderMainDetailView

urlpatterns = [
    url(r'^cashbox/$', CashBoxInputView.as_view(), name='cashbox'),
    url(r'^cashbox/(?P<id>[\w-]+)/$', CashBoxInputDetailView.as_view(), name='cashbox'),

    url(r'^cashboxlog/$', CashBoxLogView.as_view(), name='cashboxlog'),
    url(r'^cashboxlog/(?P<id>[\w-]+)/$', CashBoxLogDetailView.as_view(), name='cashboxlogdetail'),
    url(r'^cashboxlogbyoperate/(?P<operate>[\w-]+)/$', CashBoxLogByOperateView.as_view(), name='cashboxlogbyoperate'),

    url(r'^ordermain/$', OrderMainView.as_view(), name='ordermain'),
    url(r'^ordermain/(?P<id>[\w-]+)/$', OrderMainDetailView.as_view(), name='ordermain'),
]
