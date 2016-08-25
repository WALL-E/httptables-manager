#!/bin/bash

yum groupinstall -y "Development Tools"
yum -y install python34
yum -y install mariadb mariadb-server mariadb-devel
yum -y install python34-devel.x86_64

# curl https://bootstrap.pypa.io/get-pip.py | python3.4
python3.4 utils/get-pip.py
pip3 install Django==1.9.5
pip3 install mysqlclient
pip3 install djangorestframework
pip3 install markdown
pip3 install django-filter
pip3 install requests
pip3 install django-suit==0.2.21
