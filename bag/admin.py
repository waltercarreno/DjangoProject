from django.contrib import admin

# Register your models here.
from bag.models import ShopCart


class ShopCartAdmin(admin.ModelAdmin):
        list_display = (
        'product',
        'quantity',
        'price',
        'amount',
        'user',
    )



admin.site.register(ShopCart,ShopCartAdmin)
