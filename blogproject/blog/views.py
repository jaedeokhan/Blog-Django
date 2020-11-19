from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def test(request):

    return render(request, 'test.html')

def lists(request):
    
    return render(request, 'listing.html')

def post(request):

    return render(request, 'post.html')