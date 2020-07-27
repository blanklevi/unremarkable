from django.contrib import admin
from .models import Post, PostImage
from Users.models import User
from Shop.models import Category, Customer, Product, Order, OrderItem, ShippingAddress, ProductSize
from Marketing.models import Signup

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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Marketing App
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass

# Change the site header
admin.site.site_header = 'NotRemarkable Admin Dashboard'
