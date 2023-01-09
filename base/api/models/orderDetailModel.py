from django.db import models
from .categoryModel import Category
from .orderModel import Order
from .productModel import Product
from django.db.models import ManyToManyField


# Create your models here.

# quantity = models.DecimalField(max_digits=2,decimal_places=0,default=0)


class OrderDetail(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=False,blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False,blank=False)
    amount= models.IntegerField(default=1, null=True,blank=True)
    total = models.IntegerField(default=1, null=True,blank=True)

    def __str__(self):
     	return f'ID: {self._id}, Order id: {self.order_id._id}, User id: {self.order_id.user_id.id}, Username: {self.order_id.user_id.username}, Product id: {self.product_id._id}, Product desc: {self.product_id.desc}, Product amount: {self.amount}, Total: {self.total}'