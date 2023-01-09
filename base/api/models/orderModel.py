from django.db import models
from django.contrib.auth.models import User
# from .orderDetailModel import OrderDetail


# Create your models here.
#    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False,related_name="+")


class Order(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False)
    createdTime=models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0, null=True,blank=True)
    # total = models.DecimalField(max_digits=4,decimal_places=2,default=0, null=True,blank=True)


    def __str__(self):
     	return f'ID: {self._id}, User id: {self.user_id.id}, Username: {self.user_id.username}, CreatedTime: {self.createdTime}, Total: {self.total}'