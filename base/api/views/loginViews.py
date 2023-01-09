from email.policy import default
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth import logout



# singin
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['staff'] = user.is_staff
        token['superuser'] = user.is_superuser
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# register/signup
@api_view(['POST'])
def register(request):
    try:
        is_admin= request.data["admin"]
    except:
        is_admin=0
    print(is_admin)
    User.objects.create_user(username= request.data["username"],email=request.data["email"],password=request.data["password"],is_superuser=is_admin,is_staff=request.data["staff"])
    # print( request.data["username"])
    # print( request.data["email"])
    # print(request.data["password"])
    return Response("Registration done")


# Logout
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myLogout(request):
    logout(request)
    return Response("logged out")




@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)