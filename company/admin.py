from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    filter_fields = [
            "id", 
            "brand", 
            "product_name", 
            "date",
            "description", 
            "category", 
            "price", 
            "condition", 
            "delivery_available", 
            "discount", 
            "product_count"]
class WishListAdmin(admin.ModelAdmin):
    filter_fields = ("id", "product_id","product_name", "date")

admin.site.register(Product, ProductAdmin)
admin.site.register(WishList, WishListAdmin)
