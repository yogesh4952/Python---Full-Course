from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL to display the list of posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for full post
]
