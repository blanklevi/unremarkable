from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage

def blog_view(request):
    posts = Post.objects.all()
    if request.session['log_email'] != []:
        logged_user = request.session['log_email']
        sign_in_button = []
    else:
        logged_user = []
        sign_in_button = ["Levi is the best"]
    context = {
        'posts': posts,
        'logged_user': logged_user,
        'sign_in_button': sign_in_button,
    }
    return render(request, 'blog.html', context)

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'photos': photos,
    }
    return render(request, 'detail.html', context)

