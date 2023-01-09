from rest_framework.serializers import ModelSerializer
from ..models.orderModel import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
 
    def getOrder(self,obj):
        return {
                "id":obj._id,
                "user_id":obj.user._id,
                "user_name":obj.user.username,
                "createdTime":obj.createdTime,
            }
    
    def getOldOrders(self,obj):
        return {

                "createdTime":obj.createdTime,
                "total" :obj.total,
            }

