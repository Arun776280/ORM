from django.contrib import admin
from .models import Order   # ONLY import models

class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'ItemName', 'OrderQty', 'TotalAmount')

admin.site.register(Order, OrderAdmin)