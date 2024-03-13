# TKP Quiz
> Quiz website for Tran Ky Phong High School

<br>

# Development
Program language | Framework | Database
--- | --- | --- |
Python 3.11 | FastAPI 3.0 | SQLite3

<br>

# Build server
### Install the python package
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
alembic upgrade head
```

<br>

# Run server
### Change the directory to src folder
```bash
cd src
```

### Run server
```bash
uvicorn main:app
```
> **Note:**
> * Add flag `--reload` to reload the server after change code
> * Add flag `--port` to setup port number. Example: `--port 80`
