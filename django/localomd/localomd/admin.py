from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.template.response import TemplateResponse

from localomddata.admin import VendingMachineAdmin, ProductCategoryAdmin, ProductProviderAdmin, ProductAdmin, SlotAdmin, \
    OrderMainAdmin, MoneyChargeAdmin, VendingMachineTypeAdmin
from localomddata.models import VendingMachine, ProductProvider, ProductCategory, OrderMain, Slot, Product, MoneyCharge, \
    VendingMachineType


class OMDSite(AdminSite):
    site_header = '售货机后台管理'
    site_title = 'zhandian title'

admin_omd = OMDSite(name='localomd')

admin_omd.register(User, UserAdmin)
admin_omd.register(Group, GroupAdmin)
admin_omd.register(VendingMachineType, VendingMachineTypeAdmin)
admin_omd.register(VendingMachine, VendingMachineAdmin)
admin_omd.register(ProductProvider, ProductProviderAdmin)
admin_omd.register(ProductCategory, ProductCategoryAdmin)
admin_omd.register(Product, ProductAdmin)
admin_omd.register(Slot, SlotAdmin)
admin_omd.register(MoneyCharge, MoneyChargeAdmin)
admin_omd.register(OrderMain, OrderMainAdmin)