from rest_framework.serializers import ModelSerializer
from ..models.productModel import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
 
    def updateProduct(self,obj):
        return {
                # "id":obj._id,
                # "user_id":obj.user._id,
                "category_id":obj.category._id,
                "desc":obj.desc,
                "price":obj.price,
                "image":str(obj.image),
                
            }


