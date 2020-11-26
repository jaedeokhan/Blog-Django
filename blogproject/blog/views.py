from django.shortcuts import render
from blog.models import Post, Category
from django.views import generic
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

class PostListView(generic.ListView):
    model = Post
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_total'] = Post.objects.count()
        context['post_category'] = Category.objects.all()
        return context

def test(request):

    return render(request, 'test.html')

def lists(request):
    
    return render(request, 'listing.html')

def post(request):

    return render(request, 'post.html')