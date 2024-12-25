from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse("HtmlContent")

def about(request):
  return HttpResponse("<h1> Hancy ko bau 123 </h1>")