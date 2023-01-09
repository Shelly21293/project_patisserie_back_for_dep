from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models.productModel import Product
from ..models.categoryModel import Category
from ..models.orderModel import Order
from ..models.orderDetailModel import OrderDetail
from ..serialization import categorySerialize, productSerialize,orderSerialize,orderDetailSerialize
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Authenticated
# GET 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrdersForUser(request):
    user = request.user
    oldOrders= user.order_set.all()
    serializer = orderSerialize.OrderSerializer(oldOrders, many=True)

    # serializer = orderSerialize.OrderSerializer.getOldOrders(oldOrders, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderDetails(request, id=0):
    order_id = Order.objects.get(_id=id)
    print(id)
    print(order_id)
    orderDetails=OrderDetail.objects.filter(order_id=order_id)
    print(orderDetails)
    serializer = orderDetailSerialize.OrderDetailSerializer(orderDetails, many=True)
    # serializer = orderDetailSerialize.OrderDetailSerializer().getOrderDetail(orderDetails)
    return Response(serializer.data)


# POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrder(request):
    order= request.data
    user = request.user
    print(user)
    order_total=0
    for x in order:
        prod_total= x["total"]
        order_total= order_total + int(prod_total)
    # total_order= request.data[""]
    new_order_id= Order.objects.create(user_id=user, total=order_total)
    print(order)
    for x in order:
        print(x)
        prod_id=Product.objects.get(_id=x["_id"])
        prod_amount= x["amount"]
        prod_total= x["total"]
        # category_id=Category.objects.get(_id=x["category_id"])
        OrderDetail.objects.create(order_id=new_order_id,product_id=prod_id,amount= prod_amount, total=prod_total)
    return Response("Order created")



# Admin
# GET all orders
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getOrders(request):
    orders = Order.objects.all()
    serializer = orderSerialize.OrderSerializer(orders, many=True)
    return Response(serializer.data)

# GET orderdetails per order
# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def getOrderDetails(request, id=0):
#     order_id = Order.objects.get(_id=id)
#     orderDetails=OrderDetail.objects.get(order_id=order_id)
#     serializer = orderDetailSerialize.OrderDetailSerializer(orderDetails, many=True)
#     return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrder(request, id=0):
    if int(id) > 0:
        order = Order.objects.get(_id=id)
        order.delete()
        return Response("Order deleted")
    else:
        order = Order.objects.all()
        order.delete()
        return Response("All orders has been deleted")

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def updateOrderDetail(request, id=0):
    if int(id) > 0:
        # order_id = Order.objects.get(_id=id)
        orderDetail=OrderDetail.objects.get(_id=id)
        
        if "product_id" in request.data:
            orderDetail.product_id=request.data["product_id"]

        if "quantity" in request.data:
            orderDetail.quantity=request.data["quantity"]

        orderDetail.save()
        return Response("Order updated")
    else: 
        return Response("Order to update was not selected")



