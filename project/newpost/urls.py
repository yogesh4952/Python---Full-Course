from django.urls import path
from .views import newpost
urlpatterns = [
  path("new",newpost,name="newPostPage")
]