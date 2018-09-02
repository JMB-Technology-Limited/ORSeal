#!/usr/bin/env bash

set -e

echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen

locale-gen

apt-get update
apt-get install -y python3 postgresql python3-pip

su --login -c "psql -c \"CREATE USER test WITH PASSWORD 'testpassword';\"" postgres
su --login -c "psql -c \"CREATE DATABASE test WITH OWNER test ENCODING 'UTF8'  LC_COLLATE='en_GB.UTF-8' LC_CTYPE='en_GB.UTF-8'  TEMPLATE=template0 ;\"" postgres

su --login -c "psql -c \"CREATE USER app WITH PASSWORD 'password';\"" postgres
su --login -c "psql -c \"CREATE DATABASE app WITH OWNER app ENCODING 'UTF8'  LC_COLLATE='en_GB.UTF-8' LC_CTYPE='en_GB.UTF-8'  TEMPLATE=template0 ;\"" postgres

pip3 install virtualenv

cd /vagrant && virtualenv .ve -p python3

echo "alias db='psql -U app app -hlocalhost'" >> /home/ubuntu/.bashrc
echo "localhost:5432:app:app:password" > /home/ubuntu/.pgpass
chown ubuntu:ubuntu /home/ubuntu/.pgpass
chmod 0600 /home/ubuntu/.pgpass
