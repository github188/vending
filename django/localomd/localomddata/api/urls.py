from django.conf.urls import url, include
from rest_framework.authtoken import views

from localomddata.api.views.coinmachine import CoinChangeListAPIView, CoinChangeCreateAPIView, CoinChangeDetailAPIView, \
    CoinChangeUpdateAPIView, CoinChangeDeleteAPIView
from localomddata.api.views.config import ConfigListAPIView, ConfigCreateAPIView, ConfigDetailAPIView, \
    ConfigUpdateAPIView, ConfigDeleteAPIView
from localomddata.api.views.group import GroupListAPIView, GroupCreateAPIView, GroupDetailAPIView, GroupUpdateAPIView, \
    GroupDeleteAPIView
from localomddata.api.views.member import MemberListAPIView, MemberCreateAPIView, MemberDetailAPIView, \
    MemberUpdateAPIView, MemberDeleteAPIView
from localomddata.api.views.moneycharge import MoneyChargeListAPIView, MoneyChargeCreateAPIView, \
    MoneyChargeDetailAPIView, MoneyChargeUpdateAPIView, MoneyChargeDeleteAPIView
from localomddata.api.views.ordermain import OrderMainDeleteAPIView, OrderMainUpdateAPIView, OrderMainDetailAPIView, \
    OrderMainCreateAPIView, OrderMainListAPIView
from localomddata.api.views.permission.permissionview import adminPermView, shutdownView
from localomddata.api.views.product import ProductListAPIView, ProductCreateAPIView, ProductDetailAPIView, \
    ProductUpdateAPIView, ProductDeleteAPIView
from localomddata.api.views.productcategory import ProductCategoryListAPIView, ProductCategoryCreateAPIView, \
    ProductCategoryDetailAPIView, ProductCategoryUpdateAPIView, ProductCategoryDeleteAPIView
from localomddata.api.views.productprovider import ProductProviderListAPIView, ProductProviderCreateAPIView, \
    ProductProviderDetailAPIView, ProductProviderUpdateAPIView, ProductProviderDeleteAPIView
from localomddata.api.views.slot import SlotListAPIView, SlotCreateAPIView, SlotDetailAPIView, SlotUpdateAPIView, \
    SlotDeleteAPIView
from localomddata.api.views.slotstatus import SlotStatusListAPIView, SlotStatusCreateAPIView, SlotStatusDetailAPIView, \
    SlotStatusUpdateAPIView, SlotStatusDeleteAPIView
from localomddata.api.views.user import UserListAPIView, UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView, \
    UserDeleteAPIView
from localomddata.api.views.vendingmachine import VendingMachineListAPIView, VendingMachineCreateAPIView, \
    VendingMachineDetailAPIView, VendingMachineUpdateAPIView, VendingMachineDeleteAPIView
from localomddata.api.views.vendingmachinetype import VendingMachineTypeListAPIView, VendingMachineTypeCreateAPIView, \
    VendingMachineTypeDetailAPIView, VendingMachineTypeUpdateAPIView, VendingMachineTypeDeleteAPIView



urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token, name='rest_framework_token'),

    url(r'^perm/$', adminPermView, name='api-perm'),
    url(r'^shutdown/$', shutdownView, name='shutdown'),

    url(r'^moneycharge/$', MoneyChargeListAPIView.as_view(), name='moneycharge'),
    url(r'^moneycharge/create/$', MoneyChargeCreateAPIView.as_view(), name='moneycharge-create'),
    url(r'^moneycharge/(?P<id>[\w-]+)/$', MoneyChargeDetailAPIView.as_view(), name='moneycharge-detail'),
    url(r'^moneycharge/edit/(?P<id>[\w-]+)/$', MoneyChargeUpdateAPIView.as_view(), name='moneycharge-update'),
    url(r'^moneycharge/delete/(?P<id>[\w-]+)/$', MoneyChargeDeleteAPIView.as_view(), name='moneycharge-delete'),

    url(r'^group/$', GroupListAPIView.as_view(), name='group'),
    url(r'^group/create/$', GroupCreateAPIView.as_view(), name='group-create'),
    url(r'^group/(?P<id>[\w-]+)/$', GroupDetailAPIView.as_view(), name='group-detail'),
    url(r'^group/edit/(?P<id>[\w-]+)/$', GroupUpdateAPIView.as_view(), name='group-update'),
    url(r'^group/delete/(?P<id>[\w-]+)/$', GroupDeleteAPIView.as_view(), name='group-delete'),

    url(r'^ordermain/$', OrderMainListAPIView.as_view(), name='ordermain'),
    url(r'^ordermain/create/$', OrderMainCreateAPIView.as_view(), name='ordermain-create'),
    url(r'^ordermain/(?P<id>[\w-]+)/$', OrderMainDetailAPIView.as_view(), name='ordermain-detail'),
    url(r'^ordermain/edit/(?P<id>[\w-]+)/$', OrderMainUpdateAPIView.as_view(), name='ordermain-update'),
    url(r'^ordermain/delete/(?P<id>[\w-]+)/$', OrderMainDeleteAPIView.as_view(), name='ordermain-delete'),

    url(r'^product/$', ProductListAPIView.as_view(), name='product'),
    url(r'^product/create/$', ProductCreateAPIView.as_view(), name='product-create'),
    url(r'^product/(?P<id>[\w-]+)/$', ProductDetailAPIView.as_view(), name='product-detail'),
    url(r'^product/edit/(?P<id>[\w-]+)/$', ProductUpdateAPIView.as_view(), name='product-update'),
    url(r'^product/delete/(?P<id>[\w-]+)/$', ProductDeleteAPIView.as_view(), name='product-delete'),

    url(r'^productcategory/$', ProductCategoryListAPIView.as_view(), name='productcategory'),
    url(r'^productcategory/create/$', ProductCategoryCreateAPIView.as_view(), name='productcategory-create'),
    url(r'^productcategory/(?P<id>[\w-]+)/$', ProductCategoryDetailAPIView.as_view(), name='productcategory-detail'),
    url(r'^productcategory/edit/(?P<id>[\w-]+)/$', ProductCategoryUpdateAPIView.as_view(),
        name='productcategory-update'),
    url(r'^productcategory/delete/(?P<id>[\w-]+)/$', ProductCategoryDeleteAPIView.as_view(),
        name='productcategory-delete'),

    url(r'^productprovider/$', ProductProviderListAPIView.as_view(), name='productprovider'),
    url(r'^productprovider/create/$', ProductProviderCreateAPIView.as_view(), name='productprovider-create'),
    url(r'^productprovider/(?P<id>[\w-]+)/$', ProductProviderDetailAPIView.as_view(), name='productprovider-detail'),
    url(r'^productprovider/edit/(?P<id>[\w-]+)/$', ProductProviderUpdateAPIView.as_view(),
        name='productprovider-update'),
    url(r'^productprovider/delete/(?P<id>[\w-]+)/$', ProductProviderDeleteAPIView.as_view(),
        name='productprovider-delete'),

    url(r'^slot/$', SlotListAPIView.as_view(), name='slot'),
    url(r'^slot/create/$', SlotCreateAPIView.as_view(), name='slot-create'),
    url(r'^slot/(?P<id>[\w-]+)/$', SlotDetailAPIView.as_view(), name='slot-detail'),
    url(r'^slot/edit/(?P<id>[\w-]+)/$', SlotUpdateAPIView.as_view(), name='slot-update'),
    url(r'^slot/delete/(?P<id>[\w-]+)/$', SlotDeleteAPIView.as_view(), name='slot-delete'),

    url(r'^slotstatus/$', SlotStatusListAPIView.as_view(), name='slot'),
    url(r'^slotstatus/create/$', SlotStatusCreateAPIView.as_view(), name='slot-create'),
    url(r'^slotstatus/(?P<id>[\w-]+)/$', SlotStatusDetailAPIView.as_view(), name='slot-detail'),
    url(r'^slotstatus/edit/(?P<id>[\w-]+)/$', SlotStatusUpdateAPIView.as_view(), name='slot-update'),
    url(r'^slotstatus/delete/(?P<id>[\w-]+)/$', SlotStatusDeleteAPIView.as_view(), name='slot-delete'),

    url(r'^user/$', UserListAPIView.as_view(), name='user'),
    url(r'^user/create/$', UserCreateAPIView.as_view(), name='user-create'),
    url(r'^user/(?P<id>[\w-]+)/$', UserDetailAPIView.as_view(), name='user-detail'),
    url(r'^user/edit/(?P<id>[\w-]+)/$', UserUpdateAPIView.as_view(), name='user-update'),
    url(r'^user/delete/(?P<id>[\w-]+)/$', UserDeleteAPIView.as_view(), name='user-delete'),

    url(r'^member/$', MemberListAPIView.as_view(), name='member'),
    url(r'^member/create/$', MemberCreateAPIView.as_view(), name='member-create'),
    url(r'^member/(?P<id>[\w-]+)/$', MemberDetailAPIView.as_view(), name='member-detail'),
    url(r'^member/edit/(?P<id>[\w-]+)/$', MemberUpdateAPIView.as_view(), name='member-update'),
    url(r'^member/delete/(?P<id>[\w-]+)/$', MemberDeleteAPIView.as_view(), name='member-delete'),

    url(r'^vendingmachine/$', VendingMachineListAPIView.as_view(), name='vendingmachine'),
    url(r'^vendingmachine/create/$', VendingMachineCreateAPIView.as_view(), name='vendingmachine-create'),
    url(r'^vendingmachine/(?P<id>[\w-]+)/$', VendingMachineDetailAPIView.as_view(), name='vendingmachine-detail'),
    url(r'^vendingmachine/edit/(?P<id>[\w-]+)/$', VendingMachineUpdateAPIView.as_view(), name='vendingmachine-update'),
    url(r'^vendingmachine/delete/(?P<id>[\w-]+)/$', VendingMachineDeleteAPIView.as_view(),
        name='vendingmachine-delete'),

    url(r'^vendingmachinetype/$', VendingMachineTypeListAPIView.as_view(), name='vendingmachinetype'),
    url(r'^vendingmachinetype/create/$', VendingMachineTypeCreateAPIView.as_view(), name='vendingmachinetype-create'),
    url(r'^vendingmachinetype/(?P<id>[\w-]+)/$', VendingMachineTypeDetailAPIView.as_view(),
        name='vendingmachinetype-detail'),
    url(r'^vendingmachinetype/edit/(?P<id>[\w-]+)/$', VendingMachineTypeUpdateAPIView.as_view(),
        name='vendingmachinetype-update'),
    url(r'^vendingmachinetype/delete/(?P<id>[\w-]+)/$', VendingMachineTypeDeleteAPIView.as_view(),
        name='vendingmachinetype-delete'),

    url(r'^config/$', ConfigListAPIView.as_view(), name='config'),
    url(r'^config/create/$', ConfigCreateAPIView.as_view(), name='config-create'),
    url(r'^config/(?P<id>[\w-]+)/$', ConfigDetailAPIView.as_view(), name='config-detail'),
    url(r'^config/(?P<id>[\w-]+)/edit/$', ConfigUpdateAPIView.as_view(), name='config-update'),
    url(r'^config/(?P<id>[\w-]+)/delete/$', ConfigDeleteAPIView.as_view(), name='config-delete'),

    url(r'^coinchangelog/$', CoinChangeListAPIView.as_view(), name='coinchange'),
    url(r'^coinchangelog/create/$', CoinChangeCreateAPIView.as_view(), name='coinchange-create'),
    url(r'^coinchangelog/(?P<id>[\w-]+)/$', CoinChangeDetailAPIView.as_view(), name='coinchange-detail'),
    url(r'^coinchangelog/edit/(?P<id>[\w-]+)/$', CoinChangeUpdateAPIView.as_view(), name='coinchange-update'),
    url(r'^coinchangelog/delete/(?P<id>[\w-]+)/$', CoinChangeDeleteAPIView.as_view(), name='coinchange-delete'),
]
