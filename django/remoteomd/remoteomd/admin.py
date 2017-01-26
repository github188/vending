from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import User, Group

from remoteomddata.admin import VendingMachineAdmin, ProductCategoryAdmin, ProductProviderAdmin, ProductAdmin, SlotAdmin, \
    OrderMainAdmin, MoneyChargeAdmin, VendingMachineTypeAdmin, SlotStatusAdmin, ConfigAdmin, UserAdmin, MemberAdmin, \
    CoinMachineAdmin, LoginlogAdmin
from remoteomddata.models.Loginlog import Loginlog
from remoteomddata.models.coinmachine import CoinChangeLog
from remoteomddata.models.config import Config
from remoteomddata.models.member import Member
from remoteomddata.models.moneycharge import MoneyCharge
from remoteomddata.models.ordermain import OrderMain
from remoteomddata.models.product import Product
from remoteomddata.models.productcategory import ProductCategory
from remoteomddata.models.productprovider import ProductProvider
from remoteomddata.models.slot import Slot
from remoteomddata.models.slotstatus import SlotStatus
from remoteomddata.models.vendingmachine import VendingMachine
from remoteomddata.models.vendingmachinetype import VendingMachineType


class OMDSite(AdminSite):
    site_header = '售货机后台管理'
    site_title = 'omd backend'
    index_template = "admin/adminIndex.html"

admin_omd = OMDSite(name='remoteomd')

# Re-register UserAdmin
# admin_omd.unregister(User)
admin_omd.register(User, UserAdmin)
admin_omd.register(Member, MemberAdmin)
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
admin_omd.register(Config, ConfigAdmin)
admin_omd.register(CoinChangeLog, CoinMachineAdmin)
admin_omd.register(Loginlog, LoginlogAdmin)