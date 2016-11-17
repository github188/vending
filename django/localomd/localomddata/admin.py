from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite

from .forms import ProductTextForm

from .models import VendingMachine, ProductProvider, \
    Product, Slot, OrderMain, ProductCategory, MoneyCharge, VendingMachineType


# class OmdDateSite(AdminSite):
#     site_header = "abcdfff"
# admin_omddata = OmdDateSite(name='localomddata')

class VendingMachineTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "deliveryType", "cashBoxType", "coinBoxType", "num_SpringSlot", "num_GridSlot", "num_Cabinet"]
    list_display_links = ["deliveryType"]
    list_filter = ["deliveryType", "num_Cabinet"]
    ordering = ["deliveryType", "cashBoxType"]
    search_fields = ["deliveryType", "cashBoxType"]
    class Meta:
        model = VendingMachineType

class VendingMachineAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "vmType", "charger", "chargerTel", "installAddress", "installTime", "aliveTime"]
    list_display_links = ["slug"]
    list_filter = ["slug", "charger"]
    ordering = ["charger", "slug"]
    search_fields = ["chargerTel", "installAddress", "installTime", "aliveTime", "vmType",  "slug", "charger"]
    exclude = ['slug']
    class Meta:
        model = VendingMachine


class ProductProviderAdmin(admin.ModelAdmin):
    list_display = ["id", "companyName", "contactName", "contactTel", "siteUrl"]
    list_display_links = ["companyName"]
    list_filter = ["companyName"]
    ordering = ["companyName", "contactName"]
    search_fields = ["companyName", "contactName", "siteUrl"]
    class Meta:
        model = ProductProvider

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "catName", "parent"]
    list_display_links = ["catName"]
    list_filter = ["slug", "catName"]
    ordering = ["catName"]
    search_fields = ["slug", "catName"]

    class Meta:
        model = ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","provider", "productName", "orderPrice",  "orderCount", "orderCountUnit", "productPrice",
                    "imageRefUrl", "imageListUrl", "imageDetailUrl",# "productSumary", "productDesc",
                   "orderTime", "orderByUser", "isActive"]
    list_display_links = ["productName"]
    list_filter = ["provider", "productName", "category", "orderPrice", "orderByUser"]
    ordering = list_filter+ ["orderCount"]
    search_fields = list_filter + ["productSumary", "productDesc"]
    form = ProductTextForm
    # class Meta:
    #     model = Product


class SlotAdmin(admin.ModelAdmin):
    list_display = ["id", "vmSlug", "slotNo", "capacity", "controllType",
                    "currentItemNum", "malfunctionReportCount", "product"]
    list_display_links = ["id", "slotNo"]
    ordering = ["vmSlug", "controllType"]
    list_filter = ordering + ["slotNo"]
    search_fields = list_filter
    class Meta:
        model = Slot

class MoneyChargeAdmin(admin.ModelAdmin):
    list_display = ["id", "vmSlug", "totalAmount", "cashAmount", "coinAmount", "createTime", "updateTime"]
    list_display_links = ["id", "vmSlug", "createTime"]
    list_filter = ["vmSlug", "createTime"]
    ordering = ["-createTime"]
    search_fields = ["vmSlug", "cashAmount", "totalAmount"]
    exclude = ['totalAmount']
    class Meta:
        model = MoneyCharge

class OrderMainAdmin(admin.ModelAdmin):
    list_display = ["id", "slot", "payType", "totalPaid", "orderTime", "updateTime"]
    list_display_links = ["slot", "payType"]
    list_filter = ["slot", "orderTime"]
    ordering = ["-orderTime"]
    search_fields = ["slot", "payType"]

    class Meta:
        model = OrderMain

# admin.site.register(VendingMachine, VendingMachineAdmin)
# admin.site.register(ProductProvider, ProductProviderAdmin)
# admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Slot, SlotAdmin)
# admin.site.register(OrderMain, OrderMainAdmin)

# admin_omddata.register(VendingMachine, VendingMachineAdmin)
# admin_omddata.register(ProductProvider, ProductProviderAdmin)
# admin_omddata.register(ProductCategory, ProductCategoryAdmin)
# admin_omddata.register(Product, ProductAdmin)
# admin_omddata.register(Slot, SlotAdmin)
# admin_omddata.register(OrderMain, OrderMainAdmin)