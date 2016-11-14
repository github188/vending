from django.contrib import admin
from django import forms
from .forms import ProductTextForm

from .models import VendingMachine, ProductProvider, Product, Slot, OrderMain, ProductCategory


class VendingMachineAdmin(admin.ModelAdmin):
    list_display = ["id", "vmSku", "vmType", "charger", "num_SpringSlot", "num_GridSlot", "num_Cabinet"]
    list_display_links = ["vmSku"]
    # list_editable = ["vmSku"]
    list_filter = ["vmType", "charger"]
    ordering = ["charger", "vmType"]
    search_fields = ["vmType", "charger"]
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
    list_display = ["id", "vmSku", "catName", "parent"]
    list_display_links = ["catName"]
    list_filter = ["vmSku", "catName"]
    ordering = ["catName"]
    search_fields = ["vmSku", "catName"]

    class Meta:
        model = ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","provider", "productName", "orderPrice",  "orderCount", "orderCountUnit", "productPrice",
                    "imageRefUrl", "imageListUrl", "imageDetailUrl",# "productSumary", "productDesc",
                   "orderTime", "orderByUser", "isActive"]
    list_display_links = ["productName"]
    list_filter = ["provider", "productName", "category", "orderPrice", "orderByUser"]
    ordering = ["provider", "productName", "orderPrice", "category", "orderCount",]
    search_fields = ["provider", "productName", "category", "productSumary", "productDesc"]
    form = ProductTextForm
    # class Meta:
    #     model = Product


class SlotAdmin(admin.ModelAdmin):
    list_display = ["id", "vmSku", "slotNo", "capacity", "controllType",
                    "currentItemNum", "malfunctionReportCount", "product"]
    list_display_links = ["slotNo"]
    list_filter = ["vmSku", "slotNo", "controllType"]
    ordering = ["vmSku", "controllType"]
    search_fields = ["vmSku"]
    class Meta:
        model = Slot
        verbose_name_plural = "5. 货道详细"


class OrderMainAdmin(admin.ModelAdmin):
    list_display = ["id", "slot", "payType", "totalPaid", "orderTime", "updateTime"]
    list_display_links = ["slot", "payType"]
    list_filter = ["slot", "orderTime"]
    ordering = ["orderTime"]
    search_fields = ["slot", "payType"]

    class Meta:
        model = OrderMain
        verbose_name_plural = "6. 订单查看"

admin.site.register(VendingMachine, VendingMachineAdmin)
admin.site.register(ProductProvider, ProductProviderAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(OrderMain, OrderMainAdmin)