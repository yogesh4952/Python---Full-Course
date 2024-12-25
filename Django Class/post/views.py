from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  names = {
    "name":[
      "Aryan",
      "Yogesh",
      "Bibek"
    ]
  }
  return render(request,"post/home.html", context=names)