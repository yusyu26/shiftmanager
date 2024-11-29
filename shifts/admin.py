from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['date', 'starttime', 'endtime', 'author', 'substitute']  # 管理フォームで表示するフィールドを指定
    pass