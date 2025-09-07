from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, UserProfile
from .forms import BlogForm, UserProfileForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def Home(req):
    current_user = req.user
    posts = BlogPost.objects.filter(user=current_user)
    
    return render(req,'blog_app/home.html', {
        "posts": posts
    })
    
@login_required
def ProfileView(req):
    current_user = req.user
    blogs_posted = BlogPost.objects.filter(user=current_user.id).count()
    userprofile_data = get_object_or_404(UserProfile, id=current_user.id - 1)

    return render(req, 'blog_app/profile.html', {
        'user': current_user,
        'user_profile': userprofile_data,
        'blogs': blogs_posted
    })

@login_required
def AddPost(req):
    current_user = req.user
    posts = BlogPost.objects.filter(user=current_user)
    
    if req.method == "POST":
        form = BlogForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            BlogPost.objects.create(
                user=current_user,
                title=data['title'],
                content=data['content']
            )
            
            return redirect('add_post')
    else:
        form = BlogForm()
        
    return render(req, 'blog_app/add_blog.html', {'form': form, 'posts': posts})

@login_required
def DeletePost(req, id):
    data = get_object_or_404(BlogPost, id=id).delete()
    return redirect('add_post')

@login_required
def Logout(req):
    logout(req)
    return redirect('login')

def LoginView(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
                
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(req, username=data['username'], password=data['password'])
            if user is not None:
                login(req, user)
                return redirect('home')
        else:
            print("di valid")
    else:
        form = LoginForm(req.POST)
    return render(req, 'blog_app/login.html', {'form': form})

@login_required
def UpdatePost(req, id):
    data = get_object_or_404(BlogPost, id=id)
    
    if req.method == "POST":
        form = BlogForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=data)
    
    return render(req, 'blog_app/update_blog.html', {"form": form})

def RegisterUser(req):
    if req.method == 'POST':
        user_creds = RegisterForm(req.POST)
        user_profile = UserProfileForm(req.POST)
        
        if user_creds.is_valid() and user_profile.is_valid():
            user_creds = user_creds.cleaned_data
            user_profile = user_profile.cleaned_data
            user = User.objects.create_user(
                username=user_creds['username'],
                password=user_creds['password1'],
                email=user_creds['email']
            )
            
            UserProfile.objects.create(
                user=user,
                first_name=user_profile['first_name'],
                last_name=user_profile['last_name'],
                date_of_birth=user_profile['date_of_birth']
            )
            # example output
            # {'username': 'jerwin123', 'email': 'jerwinquijano19@gmail.com', 'password1': '122184pogi', 'password2': '122184pogi'}
            
            # {'first_name': 'Jerwin Nico', 'last_name': 'Quijano', 'date_of_birth': datetime.date(2025, 8, 5)}
            return redirect('login')
        else:
            print("di valid")
    else:
        user_creds = RegisterForm(req.POST)
        user_profile = UserProfileForm(req.POST)
    
    return render(req, 'blog_app/register.html', {
        "form1": user_creds,
        "form2": user_profile
    })