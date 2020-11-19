from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('lists/', views.lists, name='lists'),
    path('post', views.post, name='post'),
]

