from django.contrib import admin
from .api.models.productModel import Product
from .api.models.categoryModel import Category
from .api.models.orderModel import Order
from .api.models.orderDetailModel import OrderDetail


# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)



