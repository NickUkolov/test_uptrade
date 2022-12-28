from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ['name']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):

    list_display = ['name', 'menu', 'parent', 'active']
    list_display_links = ['name']
    list_filter = ['menu', 'active', 'parent']
    ordering = ['name']
    prepopulated_fields = {"slug": ("name",)}