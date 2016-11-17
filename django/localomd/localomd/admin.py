from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from localomddata.admin import VendingMachineAdmin, ProductCategoryAdmin, ProductProviderAdmin, ProductAdmin, SlotAdmin, \
    OrderMainAdmin, MoneyChargeAdmin, VendingMachineTypeAdmin, SlotStatusAdmin
from localomddata.models.moneycharge import MoneyCharge
from localomddata.models.ordermain import OrderMain
from localomddata.models.product import Product
from localomddata.models.productcategory import ProductCategory
from localomddata.models.productprovider import ProductProvider
from localomddata.models.slot import Slot
from localomddata.models.slotstatus import SlotStatus
from localomddata.models.vendingmachine import VendingMachine
from localomddata.models.vendingmachinetype import VendingMachineType


class OMDSite(AdminSite):
    site_header = '售货机后台管理'
    site_title = 'omd backend'
    index_template = "admin/adminIndex.html"

admin_omd = OMDSite(name='localomd')

admin_omd.register(User, UserAdmin)
admin_omd.register(Group, GroupAdmin)
admin_omd.register(VendingMachineType, VendingMachineTypeAdmin)
admin_omd.register(VendingMachine, VendingMachineAdmin)
admin_omd.register(ProductProvider, ProductProviderAdmin)
admin_omd.register(ProductCategory, ProductCategoryAdmin)
admin_omd.register(Product, ProductAdmin)
admin_omd.register(Slot, SlotAdmin)
admin_omd.register(SlotStatus, SlotStatusAdmin)
admin_omd.register(MoneyCharge, MoneyChargeAdmin)
admin_omd.register(OrderMain, OrderMainAdmin)