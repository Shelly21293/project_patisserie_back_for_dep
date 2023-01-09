from rest_framework.serializers import ModelSerializer
from ..models.orderDetailModel import OrderDetail


class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
 
    def getOrderDetail(self,obj):
        return {
                "order_id":obj.order._id,
                "product_id":obj.product._id,
                "product_desc":obj.product.desc,
                "category_id":obj.category._id,
                "category_desc":obj.category.desc,
                "quantity":obj.quantity,
                "total":obj.total,
                
            }

