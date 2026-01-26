from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Books(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)