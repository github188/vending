from django.contrib import admin

from coinMachine.models import CoinChargeLog


class CoinMachineAdmin(admin.ModelAdmin):
    list_display = ["id", "retData" ,"createTime"]
    list_display_links = list_display
    list_filter = ["retData"]
    ordering = ["-id"]
    search_fields = ["retData"]
    class Meta:
        model = CoinChargeLog

admin.site.register(CoinChargeLog, CoinMachineAdmin)
