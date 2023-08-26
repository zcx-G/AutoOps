from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

#基于JWT登录，登出，注册
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token':str(refresh.access_token),
                'username':user.username,
                'email':user.email,
                'mobile':user.mobile,
                'id':user.id
            })
        else:
            return Response({'msg':'用户名或密码错误'},status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
                return Response({'msg':'登出成功'})
            except Exception as e:
                return Response({'msg':'登出失败'},status=400)
        else:
            return Response({'msg':'登出失败'},status=400)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        return Response({
            'username':user.username,
            'email':user.email,
            'mobile':user.mobile,
            'id':user.id
        })

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({
                    'msg':'注册成功',
                    'username':user.username
                })
        else:
            return Response(serializer.errors,status=400)

