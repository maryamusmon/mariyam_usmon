from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, ProductImage, Product


# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 4
    fields = ('image',)


@admin.register(Product)
class ProductsModelAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
