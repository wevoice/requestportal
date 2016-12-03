from django.contrib import admin
from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Client, ClientAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Language, LanguageAdmin)


class VideoAssetInline(admin.StackedInline):
    model = models.VideoAsset
    extra = 0


class AudioAssetInline(admin.StackedInline):
    model = models.AudioAsset
    extra = 0


class DTPAssetInline(admin.StackedInline):
    model = models.DTPAsset
    extra = 0


class GraphicAssetInline(admin.StackedInline):
    model = models.GraphicAsset
    extra = 0


class RequestAdmin(admin.ModelAdmin):
    inlines = [VideoAssetInline, AudioAssetInline, DTPAssetInline, GraphicAssetInline]
    list_display = ('name', 'client', 'new_account', 'tms_or_cat_tool', 'created_date', 'requested_due_date')
admin.site.register(models.Request, RequestAdmin)
