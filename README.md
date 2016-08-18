# httptables-manager
httptables-manager is a simple model-backed API, to provide management services for [httptables](https://github.com/WALL-E/httptables)


## Compatibility of Operating System

* Centos7

## Technology Stack

* Python3
* MySQL
* Django1.95


## Restful API
create two read-write API for accessing information on the role_types and roles

* http://127.0.0.1:8080/apis/role_types
* http://127.0.0.1:8080/apis/roles



## Install

1. install base package

      run **depends.sh**

2. start MySQL 

      **systemctl start mariadb**

3. create database

      **CREATE DATABASE httptables CHARACTER SET utf8;**

4. import SQL

      MariaDB [(none)]> **use httptables**
      
      MariaDB [httptables]> **source httptables.dump.sql**

      **note**:
      * default user:`admin`
      * default password: `123456@admin`

5. start django

      run **manager/run.sh**

you can now open the API in your browser at http://127.0.0.1:8080/, and view  'role_types' and 'roles' API. If you use the login control in the top right corner you'll also be able to add, create and delete role_types,roles from the system.


## Integration with httptables
open manager/project/setting.py, modify the value of the HTTPTABLES_NOTIFY_URL.

```
HTTPTABLES_NOTIFY_URL=["http://172.28.32.105:8001/admin/notify"]
```

`172.28.32.105` is httptables's ip address, if you have multiple httptables, need to be added to this list.

