from django.urls import path
from .views import home,about
urlpatterns =[
  path("",home,name="homePage"),
  path("about",about,name="aboutPage")
]