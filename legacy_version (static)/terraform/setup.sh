!#bin/bash 

sudo apt update
sudo apt install apache2 -y
sudo apt install git -y

git clone https://github.com/sidhu2003/medease-devops
cd medease-devops && cd src 
cp -r * /var/www/html