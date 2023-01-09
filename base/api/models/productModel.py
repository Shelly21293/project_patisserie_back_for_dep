from django.db import models
from .categoryModel import Category


# Create your models here.

class Product(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=4,decimal_places=0,default=0)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    createdTime=models.DateTimeField(auto_now_add=True)
    
    fields =['_id','desc','price']
    def __str__(self):
     	return f'ID: {self._id}, Desc: {self.desc}, Price: {self.price}, Category id: {self.category_id._id}, Category desc: {self.category_id.desc}, CreatedTime: {self.createdTime}'

