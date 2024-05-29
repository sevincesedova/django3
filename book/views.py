from django.shortcuts import render
from .models import books

# Create your views here.
def home(request):
    bookk=books.objects.all()
    return render(request,'index.html', {"bookk": bookk})