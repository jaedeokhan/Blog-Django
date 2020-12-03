from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
    path('test/', views.test, name='test'),
]

