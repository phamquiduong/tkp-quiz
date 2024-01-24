@echo off

echo ----------------------------------------------------
echo             Install all pip packages
pip install -r requirements.txt

echo ----------------------------------------------------
echo      Change directory to source code directory
cd src

echo ----------------------------------------------------
echo                   Run migrate
python manage.py migrate

echo ----------------------------------------------------
echo                    Run server
set /p port="Please Input Server Port: "
python manage.py runserver 0.0.0.0:%port% --insecure
