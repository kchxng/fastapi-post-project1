## Init Python project (FastAPI)

- check python path based on macos's user

```bash
python3 -m site --user-base
```

```bash
# method 1: pipenv for large projects with many dependencies.
pip3 install pipenv # install as Global mode
pipenv shell # Activate the package or environment in the project directory before doing anything
pipenv install <libaryName> #
```

### Install Package or dependencies

```bash
pipenv install fastapi uvicorn sqlalchemy alembic pydantic asyncpg python-dotenv aiofiles psycopg2-binary
```

### Run application

```bash
# Runn server
uvicorn app.main:app --reload --port 8081
# or
uvicorn app.main:app --host 0.0.0.0 --port 8081

```

### Load ENV variables

```bash
# 2 ways to load env as
# load variables only
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
print(os.getenv("PORT"))

# Load env file and variables
from dotenv import load_dotenv, dotenv_values
config=dotenv_values(".env")
print(config['PORT'])

```

### Project structure

```bash
pro/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- api/
|   |    |-- feature/
|   |    |    |-- domain.py
|   |    |    |-- feature.py
|   |    |    |-- service.py
|   |    |-- api_v1.py
|   |-- core/
|   |    |-- config.py
|   |-- infra/
|   |    |-- __init__.py
|   |    |-- db.py
|   |    |-- metric.py
|   |    |-- setup.py
|   |-- utils/
|   |    |-- __init__.py
|   |    |-- loggger.py
|   |    |-- error.py
|-- tests/
|   |-- feature.http
|-- .env
|-- Pipfile
|-- Pipfile.lock
|-- Dockerfile
|-- docker-compose.yml
|-- Makefile
```

### Reference Documentation

- Package [here](https://pypi.org/project/psycopg2-binary)
- FastAPI [here](https://fastapi.tiangolo.com)
- Uvicorn [here](https://www.uvicorn.org/)
- Pydantic [here](https://docs.pydantic.dev/latest)
- SQLAlchemy [here](https://www.sqlalchemy.org/)

### Deployment

```bash
# Package Requirements
# Need normally install those package dependencies with pip
pip install -r requirements.txt
```

- Run a Server Manually. Refer [here](https://fastapi.tiangolo.com/deployment/manually)

```bash
fastapi run app/main.py
```

- Run Gunicorn with Uvicorn Workers. Refer [here](https://fastapi.tiangolo.com/deployment/server-workers)

```bash
pip3 install "uvicorn[standard]"
create requirements.txt
pip3 install --no-cache-dir 0r requirements.txt
uvicorn app.main.py --host 0.0.0.0 --port 8081
```

- Deploy on docker. Refer [here](https://fastapi.tiangolo.com/deployment/docker/)

```bash

# 1 -----------------------------------------------------------------
# Dockerfile
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
# ------------------------------------------------------------------

# 2 -----------------------------------------------------------------
# Dockerfile
FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt /requirements.txt

ADD ./app /code/app

RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:application", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# ------------------------------------------------------------------

docker build -t myimage .

```
