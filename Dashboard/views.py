from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .filters import PostFilter
from .models import Post, PostImage

def blog_view(request):
    posts = Post.objects.all().order_by('-created_at')
    postz = Post.objects.all()
    # if  request.session['log_email'] != []:
    #     logged_user = request.session['log_email']
    #     sign_in_button = []
    # else:
    #     # logged_user = []
    #     sign_in_button = ["Levi is the best"] 
    
    # Search Bar
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    
    # Pagination
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # User
    # user = User.objects.filter(email=logged_user)
    # print(user)
    # user_fn = user.first_name
    # request.session['first_name'] = user_fn
    # first_name = request.session['first_name']

    context = {
        'posts': posts,
        # 'logged_user': logged_user,
        # 'first_name': first_name,
        # 'sign_in_button': sign_in_button,
        'myFilter': myFilter,
        'all_posts': myFilter.qs,
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

