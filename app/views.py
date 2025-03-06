from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, RegisterForm, CommentForm

# Trang chủ Blog - Hiển thị danh sách bài viết và bình luận
def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'app/home.html', {'posts': posts, 'comment_form': comment_form})

# Chỉ user đã đăng nhập mới được tạo bài viết
@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_home')
    else:
        form = PostForm()
    return render(request, 'app/create_post.html', {'form': form})

# Chỉ user đã đăng nhập mới được bình luận
@login_required(login_url='login')
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect('blog_home')

# Đăng ký user mới
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_home')
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})

# Đăng nhập
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_home')
        else:
            return render(request, 'app/login.html', {'error': 'Sai tài khoản hoặc mật khẩu!'})
    return render(request, 'app/login.html')

# Đăng xuất
def logout_user(request):
    logout(request)
    return redirect('blog_home')