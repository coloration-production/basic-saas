# python flask boilerplate

## Startup

``` bash
# linux: source venv/bin/activate
# windows: venv\Scripts\activate
(venv)$ pip install -r requirements.txt
```

### develop

``` python
from app import app

if __name__ == '__main__':
  # Development
  app.run(debug=True, host = host, port = port)
```

``` bash
(venv)$ python main.py
```

### deploy

``` python
from gevent.pywsgi import WSGIServer
from app import app

if __name__ == '__main__':
  # Production
  http_server = WSGIServer(('0.0.0.0', port), app)
  http_server.serve_forever()
```

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

`<doing>`

## install packages

``` bash
(venv)$ pip install <package>
(venv)$ pip freeze > requirements.txt
```

