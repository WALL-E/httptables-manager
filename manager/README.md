# create tokens 

```
[vagrant@vagrant-172-28-32-105 manager]$ python3 manage.py shell
Python 3.4.3 (default, Jul  8 2016, 11:37:17)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from rest_framework.authtoken.models import Token
>>> from django.contrib.auth.models import User
>>> admin = User.objects.get(username="admin")
>>> token = Token.objects.get_or_create(user=admin)
>>> print(token)
(<Token: 5fcd69a386ae6e073e51edb941b367d703496f21>, False)
>>>
```
