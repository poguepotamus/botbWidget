echo -e "\rBuilding tailwind files, please wait."
sudo -E python manage.py tailwind build

echo -e "\nCollecting all static files to serve, please wait."
sudo -E python manage.py collectstatic --noinput

echo -e "\nRunning redis on port 6379 for channels communication." 
sudo -E docker start ed9c3d466f2f

echo -e "\nLaunching server, find widget at http://hobocutie.com/battleotbois2022/widget\n"
sudo -E /home/matthew/.local/bin/daphne -b 0.0.0.0 -p 80 botb.asgi:application
