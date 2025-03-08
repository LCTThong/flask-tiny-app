# Tyni Flask (Django-based Blogging Platform)

## 1. Thông tin cá nhân
- **Họ tên:** Phạm Duy Thông
- **Mã sinh viên:** 22664351
----
- **Họ tên:** Trương Đăng Thông
- **Mã sinh viên:** 22667231

## 2. Mô tả Project
Tyni Flask là một nền tảng blog mini sử dụng Django, cho phép người dùng:
- Đăng ký, đăng nhập, quản lý tài khoản.
- Viết, chỉnh sửa, xóa bài viết.
- Bình luận trên bài viết của người khác.
- Hỗ trợ phân trang bài viết.

## 3. Hướng dẫn cài đặt và chạy

### 🔹 **Yêu cầu hệ thống**
- Python 3.10+
- Django 4.x
- SQLite hoặc PostgreSQL (tùy chọn)

### 🔹 **Cài đặt**
#### **Cách 1: Chạy Script Cài Đặt Tự Động**
Chạy lệnh sau trên terminal (Linux/Mac) hoặc command prompt (Windows):
```sh
bash install.sh  # Nếu đang dùng Linux/Mac
install.bat      # Nếu đang dùng Windows
####**Cách 2: Cài đặt thủ công
# Clone project về máy
git clone https://github.com/DTdz59/flask-tiny-app.git/tyni_flask.git
cd tyni_flask

# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy migration
python manage.py migrate

# Tạo tài khoản admin
python manage.py createsuperuser

# Chạy server
python manage.py runserver
#bây giờ bạn có thể truy cập trang web bằng đường dẫn http://127.0.0.1:8000./blog