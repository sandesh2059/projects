from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView, Http404
from rest_framework import status

class Books(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self,request, pk):
        books = self.get_object(pk=pk)
        serializer = BookSerializer(books)
        return Response(serializer.data)

