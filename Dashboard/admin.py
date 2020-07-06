from django.contrib import admin
from .models import Post, PostImage
from Users.models import User
from Shop.models import Customer, Product, Order, OrderItem, ShippingAddress

# Dashboard App
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

# User App
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# Shop App
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    pass

# Change the site header
admin.site.site_header = 'NotRemarkable Admin Dashboard'
