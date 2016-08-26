1. sudo yum install -y httpd-devel.x86_64

2. sudo pip3 install mod_wsgi

3. mod_wsgi-express setup-server wsgi.py --port=10085 --user apache --group apache --server-root=/etc/mod_wsgi-express-10085 --url-alias static /apps/httptables-manager/manager/static

4. /etc/mod_wsgi-express-10085/apachectl [start|stop|restart]
