# TKP Quiz
> Website thi trắc nghiệm của trường THPT Trần Kỳ Phong

<br>

# Công nghệ phát triển
Ngôn ngữ lập trình | Framework | Cơ sở dữ liệu
--- | --- | ---|
[Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | [Django 4.2.8](https://docs.djangoproject.com/en/5.0/releases/4.2.8/) | [Sqlite3](https://www.sqlite.org/index.html)

<br>

# Cài đặt website
## Cài đặt Python 3.11
> - **Cách 1:** Các bạn ghé [Trang Chủ Python 3.11.7](https://www.python.org/downloads/release/python-3117/). Tiến hành tải và cài đặt.
>   - Lưu ý: Bạn phải tick vào 2 tùy chọn bên dưới của chương trình cài đặt
>   - Hình minh họa ![Hướng dẫn cài đặt](./README/Hướng%20dẫn%20cài%20đặt%20Python.png)
> - **Cách 2:** Nếu các bạn đang dùng Windows 10 trở lên. Bạn có thể cài đặt [Python trên Microsoft Store](https://apps.microsoft.com/detail/9NRWMJP3717K)
>   - Hình minh họa ![Python trên Microsolf Store](./README/Python3.11%20trên%20Store.png)


## Sao chép tệp môi trường
> - Bạn copy file `.env.example` thành file `.env`
> - Cài đặt các thông số cho hệ thống tại file `.env`.
>   - **Lưu ý:** Khi chạy server trên môi trường thực tế thì phải để `DEBUG=false`

## Cài đặt và chạy server
### Cách 1: Bằng Script có sẵn
> - **Windows**
>   - Các bạn đúp chuột vào file `run_server.bat`
> - **MacOS**
>   - Các bạn dùng terminal chạy file `run_server.command`

### Cách 2: Thủ công
> - **Lưu ý:** Các lệnh phía dưới. Nếu bạn đang dùng `MacOS` hay `Linux` thì bạn dùng `python3 và pip3` thay cho `python và pip`
> - Cài các gói thư viện:
>   ```bash
>   pip install -r requirements.txt
>   ```
> - Vào thư mục Source Code
>   ```bash
>   cd src/
>   ```
> - Cài đặt cấu trúc Database
>   ```bash
>   python manage.py migrate
>   ```
> - Chạy Server
>   ```bash
>   python manage.py runserver 0.0.0.0:80 --insecure
>   ```
>   - Trong đó: 80 là `cổng` để server chạy trên máy bạn

### Cách 3: Dùng Docker-Compose
> - Vào thư mục docker và copy file `.env.example` thành file `.env`
>   - Sửa các thông số của server để chạy docker
> - Tạo docker network cho sản phẩm
>   ```bash
>   docker network create tkp-quiz_network
>   ```
> - Chạy server
>   ```bash
>   docker-compose up --build -d
>   ```
> - Tắt server
>   ```bash
>   docker-compose down
>   ```
