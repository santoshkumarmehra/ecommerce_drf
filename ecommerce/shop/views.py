from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class UserRegistrationAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'msg': 'Registration success'})
    

class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({'msg': 'login successfull'})
        return Response(serializer.errors)



