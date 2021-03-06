from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/like', views.post_like, name='post_like'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
]