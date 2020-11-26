from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('test/', views.test, name='test'),
    # path('lists/', views.lists, name='lists'),
    path('post', views.post, name='post'),
]

