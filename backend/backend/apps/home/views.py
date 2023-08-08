from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request):
        from django.db import DatabaseError
        raise DatabaseError("mysql连接失败")



def get(request):
    import time
    return HttpResponse({"message": "hello"})
