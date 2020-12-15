import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Category
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# 블로그 리스트
class PostListView(generic.ListView):
    model = Post
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

# 블로그 상세보기
class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

# 블로그 추천수 구현
@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    is_liked = post.likes_user.filter(id=user.id).exists()
    if is_liked:
        post.likes_user.remove(user)
        message = "추천을 취소했습니다."
    else:
        post.likes_user.add(user)
        message = "추천을 성공했습니다."

    context = {'likes_count': post.count_likes_user(), 'message' : message, 'is_liked' : is_liked}
    return HttpResponse(json.dumps(context), content_type="application/json")

# 블로그 작성하기
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'image', 'user']
    template_name = "blog/post_create.html"
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

# 블로그 수정하기
class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    # context_object_name = 'post'
    fields = ['title', 'category', 'content', 'image']
    template_name = "blog/post_update.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

# 블로그 삭제하기
class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = "/"

