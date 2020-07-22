from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .filters import PostFilter
from .models import Post, PostImage
from Marketing.forms import EmailSignupForm

def blog_view(request):
    posts = Post.objects.all().order_by('-created_at')
    postz = Post.objects.all()

    # Search Bar
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    
    # Pagination
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # Newsletter
    form = EmailSignupForm()

    context = {
        'posts': posts,
        'myFilter': myFilter,
        'all_posts': myFilter.qs,
        'form': form,
    }
    return render(request, 'Dashboard/blog.html', context)

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'photos': photos,
    }
    return render(request, 'Dashboard/detail.html', context)

# About page
def about_page(request):
    context = {}
    return render(request, 'Dashboard/about.html', context)
