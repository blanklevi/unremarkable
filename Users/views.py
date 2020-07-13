from django.shortcuts import render, redirect
from Users.models import User
from Dashboard.models import Post, PostImage
from django.contrib import messages
import bcrypt
from Users.forms import UserRegisterForm


def index(request):
    # request.session['log_email'] = []
    # request.session['log_password'] = []
    # request.session['log_first_name'] = []
    # request.session['log_last_name'] = []
    return redirect("/")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in!')
            return redirect('login')
    else: 
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, "Users/register.html", context)

def login_page(request):
    return render(request, "Users/login.html")

def log_in(request):
    errors = User.objects.log_in_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/users/login")
    else:
        if request.method == "POST":
            log_email = request.POST['log_email']
            log_pw = request.POST['log_pw']
            if User.objects.filter(email=log_email):
                request.session['log_email'] = log_email
                request.session['log_pw'] = log_pw
                return redirect("/")


# def register(request):
#     errors = User.objects.reg_validator(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/users/register')
#     else:
#         if request.method == "POST":
#             first_name = request.POST['first_name']
#             last_name = request.POST['last_name']
#             email = request.POST['email']
#             pw = request.POST['password']
#             confirm_pw = request.POST['confirm_pw']
#             pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
#             # confirm password stuff here
#             if bcrypt.checkpw(confirm_pw.encode(), pw_hash.encode()) == True:
#                 User.objects.create(first_name=first_name, last_name=last_name,
#                                     email=email, password=pw_hash)
#                 request.session['log_email'] = email
#                 request.session['log_password'] = pw_hash
#                 request.session['log_first_name'] = first_name
#                 request.session['log_last_name'] = last_name
#             else:
#                 errors['pwconfirm'] = "Passwords did not match!"
#                 if len(errors) > 0:
#                     for key, value in errors.items():
#                         messages.error(request, value)
#                     return redirect('/register')
#     return redirect('/')


def successful_log_in(request):
    if request.session['log_email'] == []:
        return redirect('/')

    else:
        logged_user = User.objects.filter(email=request.session['log_email'])
        user_first_name = logged_user[0].first_name
    
        context = {
            "user_first_name": user_first_name,
            "user_admin": user_admin,
        }
        print(f"entire context: {context}")
        return redirect('/')

def log_out(request):
    request.session['log_email'] = []
    request.session['log_pw'] = []
    return redirect('/')
