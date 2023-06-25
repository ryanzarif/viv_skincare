from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')
    list_filter = ('create',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'available', 'unit_price', 'discount', 'total_price',
                    'create', 'update', ]
    list_filter = ('available', 'category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
