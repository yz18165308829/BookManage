from django.shortcuts import render

# Create your views here.
from .models import Book

from django.http import HttpResponse


def index(request):
    booklist = Book.objects.all()
    return render(request, 'bookApp/index.html', {'booklist': booklist})


def detail(request, id):
    book = Book.objects.get(pk=id)
    book.views +=1
    book.save()
    return render(request,'bookApp/detail.html',{'book':book})
