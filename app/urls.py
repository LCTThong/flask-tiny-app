from django.urls import path
from . import views  # Import views từ thư mục app

urlpatterns = [
    path('', views.blog_home, name='blog_home'),  # Trang danh sách bài viết
    path('create/', views.create_post, name='create_post'),  # Form tạo bài viết
    path('register/', views.register, name='register'),  # Đăng ký user mới
    path('login/', views.login_user, name='login'),  # Đăng nhập
    path('logout/', views.logout_user, name='logout'),  # Đăng xuất
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),  # Bình luận bài viết
    path('logout/', views.logout_user, name='logout'),

]