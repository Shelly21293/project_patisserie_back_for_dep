from rest_framework.serializers import ModelSerializer
from ..models.categoryModel import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
 
    def getCategory(self,obj):
        return {
                "id":obj._id,
                "desc":obj.desc,
                
            }