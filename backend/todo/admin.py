from django.contrib import admin

from .models import Category, TodoItem


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(TodoItem, TodoAdmin)
admin.site.register(Category)
