#!/bin/bash

echo "== BEGIN =="

echo "== Upgrading pip =="
pip install --user --upgrade pip

echo "== Installing virtualenv =="
pip install --user virtualenv

echo "== Creating virtualenv 'env' =="
virtualenv env

echo "== Activating virtualenv 'env' =="
source env/bin/activate

echo "== Installing requirements =="
pip install django
pip install psycopg2 # Needed for postgresql support
pip install django-polymorphic # Needed for polymorphic model support
                               # (allows querying of parent models to return children

echo "== Creating symbolic links =="
ln -s env/bin/activate activate

echo "** Please source activate (-> env/bin/activate) **"
echo "== END =="
