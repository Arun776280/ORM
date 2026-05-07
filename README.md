# Ex01 Django ORM Web Application
## Date: 07.05.26

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Order   

class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'ItemName', 'OrderQty', 'TotalAmount')

admin.site.register(Order, OrderAdmin)

models.py

from django.db import models
from django.contrib import admin
class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.DateTimeField()
    ItemName = models.CharField(max_length=255)
    OrderQty = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DeliveryAddress = models.TextField()

    def _str_(self):
        return f"Order {self.OrderID} - {self.ItemName
```



## OUTPUT
![alt text](<Screenshot 2026-05-03 135622.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
