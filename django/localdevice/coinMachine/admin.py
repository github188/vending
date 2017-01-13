from django.contrib import admin

from coinMachine.models import CoinMachineInput, CoinMachineOutput

class CoinMachineInAdmin(admin.ModelAdmin):
    list_display = ["id","payoutCnt","inputDesc", "createTime"]
    list_display_links = list_display
    list_filter = ["payoutCnt"]
    ordering = ["-id"]
    search_fields = ["inputDesc"]
    class Meta:
        model = CoinMachineInput


class CoinMachineOutAdmin(admin.ModelAdmin):
    list_display = ["id", "input", "outputDesc", "createTime"]
    list_display_links = list_display
    list_filter = ["id"]
    ordering = ["-id"]
    search_fields = ["input", "outputDesc"]

    class Meta:
        model = CoinMachineOutput


admin.site.register(CoinMachineInput, CoinMachineInAdmin)
admin.site.register(CoinMachineOutput, CoinMachineOutAdmin)