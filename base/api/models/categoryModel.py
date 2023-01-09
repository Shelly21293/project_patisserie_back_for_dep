from django.db import models


# Create your models here.

class Category(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    desc =models.CharField(max_length=50,null=False,blank=False)

    
    # fields =['_id','desc','price']
    def __str__(self):
     	return f'Category id: {self._id}, Category desc: {self.desc}'