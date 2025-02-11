from django.contrib import admin
from django.utils.html import format_html
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_imagem')

    def preview_imagem(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>'.format(obj.image.url))
        return "Sem imagem"

# Register your models here.
admin.site.register(Notice, NoticeAdmin)