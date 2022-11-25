echo -e "\rBuilding tailwind files, please wait."
python manage.py tailwind build

echo -e "\nCollecting all static files to serve, please wait."
python manage.py collectstatic --noinput

echo -e "\nLaunching server, find widget at http://hobocutie.com/botb/widget\n"
sudo -E /home/matthew/.local/bin/daphne -b 0.0.0.0 -p 80 botb.asgi:application
