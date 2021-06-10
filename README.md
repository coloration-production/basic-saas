# python flask boilerplate

## Server

### Startup

``` bash
# develop
server$ python3 -m venv venv

server$ sqlite3
> .open db.sqlite
> .databases # to check
> .quit

server$ source venv/bin/activate # linux: 
server$ venv\Scripts\activate # windows: 

server(venv)$ pip install -r requirements.txt
server(venv)$ python main.py
```

### Deploy

1. supervisor

``` bash
# /etc/supervisord.d/<project>.ini

command   = /usr/bin/python /home/www/<project>/main.py
directory = /home/www/<project>/
```

```bash
$ supervisorctl start <project>
$ supervisorctl shutdown
```

2. docker

``` bash
$ docker compose up -d
```

### Feature

- [x] configure env for Development, Testing and Production
  - `config`
- [x] route's demo 
  - `application.routes.demo`
- [x] SQLAlchemy's demo with sqlite 
  - `application.models.user` 
  - `application.models.role` 
  - `application.routes.user`
  - `application.routes.role`
  - `application.routes.access`
- [ ] schedule's demo
- [ ] permissions
- [x] JWT for RESTful
- [x] Insomnia.yaml for HTTP Client [Insomnia](https://insomnia.rest/)
- [x] for docker

### Note

1. switch develop/project enviornment

``` python
# server/config.py
current = DevelopmentConfig
# or 
current = ProductionConfig
# or
current = TestingConfig
```

2. install package

``` bash
(venv)$ pip install <package>
(venv)$ pip freeze > requirements.txt
```

### Lib

- [Flask-JWT](https://pythonhosted.org/Flask-JWT/)


## Client


### Startup

``` bash
# develop
client$ npm install
client$ npm run dev

# build
client$ npm run build
```

### Deploy

1. maunal

2. docker

`doing`


### Feature

- api
  - [x] access
  - [ ] user
  - [ ] role
  - [ ] permission
- router
  - [x] basic change
  - [x] 401 redict `/access/signin`
  - [x] sidebar configuration
- ui
  - [x] sign in 
  - [ ] change password
  - [ ] user
  - [ ] role
  - [ ] sidebar
  - [ ] header
  - [ ] base entity

### Lib

- [Vitesse](https://github.com/antfu/vitesse)