from django.urls import path
from .import views

urlpatterns = [
    path('', views.fileView, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post', views.post1, name='post1'),
    path('post', views.post2, name='post2'),
    path('post', views.post3, name='post3'),
    ]
