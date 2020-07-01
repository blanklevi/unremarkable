from django.contrib import admin
from .models import Post, PostImage


# Image uploading things
class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

# Change the site header
admin.site.site_header = 'UnRemarkable Admin Dashboard'