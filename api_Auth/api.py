from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, response
from rest_framework.views import APIView

from api_Auth.serializer import UserSerializer

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return response({"statusCode": 403, 'errors': serializer.errors, 'message': 'Some'})
        
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])

        token_obj, _ =  Token.objects.get_or_create(user=user)

        return response({"statusCode": 200, 'payload': serializer.data, 'token': str(token_obj)})