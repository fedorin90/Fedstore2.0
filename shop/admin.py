from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'get_html_photo', 'price', 'stock', 'available', 'created', 'updated']
    list_display_links = ['name', 'slug']
    search_fields = ('name', 'description',)
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "Image"


admin.site.register(Product, ProductAdmin)


