from django.contrib import admin

# Register your models here.
from controlBoard.models import ControlBoardInput, ControlBoardOutput


class ControlBoardInAdmin(admin.ModelAdmin):
    list_display = ["id", "slotNo" ,"turnCnt","inputDesc", "createTime"]
    list_display_links = list_display
    list_filter = ["slotNo"]
    ordering = ["-id"]
    search_fields = ["inputDesc"]
    class Meta:
        model = ControlBoardInput


class ControlBoardOutAdmin(admin.ModelAdmin):
    list_display = ["id", "input", "outputDesc", "createTime"]
    list_display_links = list_display
    list_filter = ["id"]
    ordering = ["-id"]
    search_fields = ["input", "outputDesc"]

    class Meta:
        model = ControlBoardOutput


admin.site.register(ControlBoardInput, ControlBoardInAdmin)
admin.site.register(ControlBoardOutput, ControlBoardOutAdmin)