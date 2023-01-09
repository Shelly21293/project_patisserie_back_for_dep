from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models.productModel import Product
from ..models.categoryModel import Category
from ..serialization import categorySerialize, productSerialize
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# for super user only
# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda u: u.is_superuser)


# Anonymous
# GET 
@api_view(['GET'])
def getCategories(request, id=0):
    if int(id) > 0:  # return single cat -READ
        # print("1")
        cat = Category.objects.filter(_id=id)
        # print("2")
    else:  # get All -READ
        cat = Category.objects.all()

    serializer = categorySerialize.CategorySerializer(cat, many=True)      
    return Response(serializer.data)
 

# Admin
# create
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addCategory(request):
    serializer = categorySerialize.CategorySerializer(data=request.data)  
    if( serializer.is_valid()):
        serializer.save()
    else:
        return Response("Category was not saved, check data")
    return Response("Category added")


# delete
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategory(request, id=0):
    if int(id) > 0: 
        cat = Category.objects.get(_id=id)
        cat.delete()
        return Response("Category deleted")
    else:
        return Response("Category to delete was not selected")

# UPDATE
@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def updateCategory(request, id=0):
    if int(id) > 0: 
        cat = Category.objects.get(_id=id)
        if "desc" in request.data:
            cat.desc=request.data["desc"]

        cat.save()
        return Response("Category updated")
    else: 
        return Response("Category to update was not selected")


