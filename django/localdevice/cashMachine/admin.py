from django.contrib import admin

# Register your models here.
from cashMachine.models.cashboxlog import CashboxLog
from cashMachine.models.cashboxoperate import CashboxOperate
from cashMachine.models.ordermain import OrderMain


class CashboxOperateAdmin(admin.ModelAdmin):
    list_display = ["id", "operateName" ,"operateData", "createTime"]
    list_display_links = list_display
    list_filter = ["operateName"]
    ordering = ["-id"]
    search_fields = ["operateName"]
    class Meta:
        model = CashboxOperate

class CashboxLogAdmin(admin.ModelAdmin):
    list_display = ["id", "operate", "getOperateName", "operateStatus", "retData", "createTime"]
    list_display_links = list_display
    list_filter = ["operateStatus", "id"]
    ordering = ["-id"]
    search_fields = ["operate", "operateStatus", "retData"]

    def getOperateName(self, obj):
        return dict(CashboxOperate.operateChoice).get(obj.operate.operateName)
    getOperateName.short_description = "操作名"

    class Meta:
        model = CashboxLog

class OrderMainAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'product','itemCount', 'orderNo', 'payType', 'status', 'totalPaid','changeLeft','coinLeft', 'createTime']
    list_display_links = list_display
    list_filter = ["slot", "product", "payType",]
    ordering = ["-id"]
    search_fields = list_display

    class Meta:
        model = OrderMain

admin.site.register(CashboxOperate, CashboxOperateAdmin)
admin.site.register(CashboxLog, CashboxLogAdmin)
admin.site.register(OrderMain, OrderMainAdmin)