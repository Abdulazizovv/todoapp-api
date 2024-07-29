from django.contrib import admin
from .models import TodoList, TodoCategory, TodoItem


class TodoListAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['created', 'updated']
    list_per_page = 10


class TodoCategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['created', 'updated']
    list_per_page = 10


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created', 'updated', 'todo_list']
    search_fields = ['title', 'description']
    list_filter = ['created', 'updated']
    list_per_page = 10


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoCategory, TodoCategoryAdmin)
admin.site.register(TodoItem, TodoItemAdmin)