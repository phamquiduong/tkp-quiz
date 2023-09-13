# TKP Quiz (chưa hoàn thành)
Website thi trắc nghiệm mẫu được dựng bằng Python Django và SQLite3


## Cài đặt python
Các bạn tham khảo video [Hướng dẫn cài đặt Python cho hệ điều hành Windows 7, 8, 10, 11 (32 bit & 64 bit); MacOS; Linux](https://www.youtube.com/watch?v=tCjlrIowuDk)


## Cài đặt môi trường ảo
Các bạn có thể tham khảo một số video sau:
- [Hướng dẫn Tạo Virtual Environment trong Python](https://www.youtube.com/watch?v=jOUUqDGogAo)
- [Nếu bạn dùng VScode bạn có thể tham khảo các sau](https://code.visualstudio.com/docs/python/environments)


## Dựng server
### Cài đặt gói thư viện
Các bạn chạy lệnh
```bash
pip install -r requirements.txt
```

### Sau đó có các bạn chuyển đến thư mục src/
```bash
cd src/
```

### Tự động tạo migrations file
```bash
python manage.py makemigrations
```

### Chạy các migrations file
```bash
python manage.py migrate
```

### Thu thập static files
Xóa thư mục static files nếu có
```bash
# Với hệ điều hành Windows. Chạy lệnh sau xác nhận lại bằng cách nhấn ENTER
rmdir ../static/
```
Thu thập lại static files mới
```bash
python manage.py collectstatic --noinput
```

## Chạy server
```bash
python manage.py runserver 0.0.0.0:80
```
### Lưu ý:
- 0.0.0.0 là địa chỉ máy tính
- 80 là cổng để chạy

### Giờ các bạn có thể vào `localhost` trên trình duyệt để sử dụng trang web


## Chúc các bạn thành công!