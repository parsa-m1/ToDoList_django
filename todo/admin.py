from django.contrib import admin

from .models import *

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done')
    list_filter = ('is_done',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}



