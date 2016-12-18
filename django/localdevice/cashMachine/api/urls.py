from django.conf.urls import url

from cashMachine.api.views import CashBoxInputView


urlpatterns = [
    url(r'^cashbox/$', CashBoxInputView.as_view(), name='start'),

]
