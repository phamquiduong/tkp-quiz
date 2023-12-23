@echo off

echo "----------------------------------------------------"
echo "            Install all pip packages"
pip install -r requirements.txt
echo "\n"

echo "----------------------------------------------------"
echo "     Change directory to source code directory"
cd src
echo "\n"

echo "----------------------------------------------------"
echo "                  Run migrate"
python manage.py migrate
echo "\n"

echo "----------------------------------------------------"
echo "                   Run server"
set /p port="Please Input Server Port: "
python manage.py runserver 0.0.0.0:%port% --insecure
