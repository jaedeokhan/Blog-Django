from django.shortcuts import render
from blog.models import Post, Category
from django.views import generic
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

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

# 블로그 작성하기
class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'image']
    template_name = "blog/post_create.html"
    success_url = "/blog/posts"

# 블로그 수정하기
class PostUpdateView(generic.UpdateView):
    model = Post
    # context_object_name = 'post'
    fields = ['title', 'category', 'content', 'image']
    template_name = "blog/post_update.html"
    success_url = "/blog/posts"

# 블로그 삭제하기
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = "/blog/posts"


def test(request):

    return render(request, 'test.html')

# def lists(request):
    
#     return render(request, 'listing.html')