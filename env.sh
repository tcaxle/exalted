#!/bin/bash

echo "== BEGIN =="

echo "== Upgrading pip =="
pip3.8 install --user --upgrade pip

echo "== Installing virtualenv =="
pip3.8 install --user virtualenv

echo "== Creating virtualenv 'env' =="
python3.8 -m virtualenv env

echo "== Activating virtualenv 'env' =="
source env/bin/activate

echo "== Installing requirements =="
pip3.8 install django
pip3.8 install psycopg2 # Needed for postgresql support
pip3.8 install django-polymorphic # Needed for polymorphic model support
                               # (allows querying of parent models to return children

echo "== Creating symbolic link activate -> env/bin/activate =="
ln -s env/bin/activate activate

echo "** Please source activate (-> env/bin/activate) **"
echo "== END =="
