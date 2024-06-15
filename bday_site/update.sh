# update env
sudo apt-get update

# activate virtual environment
source bday/bin/activate

# change directory to the project root
cd Bday_2024--customWordCloudSite

# update repo
git fetch origin
git reset --hard origin/main

# runserver
cd bday_site
echo "go to the '52.14.52.212:8000' in your browser to see the site."
python3 manage.py runserver 0.0.0.0:8000
