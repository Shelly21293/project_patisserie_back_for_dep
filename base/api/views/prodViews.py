from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models.productModel import Product
from ..models.categoryModel import Category
from ..serialization import categorySerialize, productSerialize
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Anonymous
# GET 
@api_view(['GET'])
def getProducts(request, id=0):
    if int(id) > 0:  # return single prod -READ
        prod = Product.objects.filter(_id=id)
    else:  # get All -READ
        prod = Product.objects.all()
    serializer = productSerialize.ProductSerializer(prod, many=True)      
    return Response(serializer.data)

@api_view(['GET'])
def getProductsPerCategoty(request, cat_id=0):
    if int(cat_id) > 0:  # return prods per category -READ
        prod = Product.objects.filter(category_id_id=int(cat_id))
    else:  # get All prods -READ
        prod = Product.objects.all()
    serializer = productSerialize.ProductSerializer(prod, many=True)      
    return Response(serializer.data)
 
    
 

# Admin
# create
@api_view(['POST']) 
@permission_classes([IsAdminUser])
def addProduct(request):
    serializer = productSerialize.ProductSerializer(data=request.data)  
    if( serializer.is_valid()):
        serializer.save()
    else:
        return Response("product was not saved, check data")
    return Response("Product added")


# delete
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, id):
    prod = Product.objects.get(_id=id)
    prod.delete()
    return Response("Product deleted")
    

# # delete
# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def deleteProduct(request, id=0):
#     if int(id) > 0: 
#         prod = Product.objects.get(_id=id)
#         prod.delete()
#         return Response("Product deleted")
#     else:
#         return Response("Product to delete was not selected")

# UPDATE
@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def updateProduct(request, id=0):
    
    if int(id) > 0:
        prod = Product.objects.get(_id=id)
        # print(prod)
        if "category_id" in request.data:
            prod.category_id= Category.objects.get(_id= request.data["category_id"])
        
        if "desc" in request.data:
            prod.desc=request.data["desc"]

        if "price" in request.data:
            prod.price=request.data["price"]
        
        if "image" in request.data:
            prod.image=request.data["image"]

        prod.save()
        
        return Response("Product updated")
    else: 
        return Response("Product to update was not selected")


