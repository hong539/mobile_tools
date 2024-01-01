# local_library_website

## To-do-list

* Monitor and alert
    * [Sentry](https://github.com/getsentry)
        * [Rust Development at Sentry](https://develop.sentry.dev/rust/)
        * [self-hosted](https://develop.sentry.dev/self-hosted/)
        * [Python Error and Performance Monitoring for Django web apps](https://sentry.io/for/python/?original_referrer=https%3A%2F%2Fgithub.com%2F&platform=sentry.python.django)
        * Real-time crash reporting for your web apps, mobile apps, and games.
* Benchmark
    * [Extreme HTTP Performance Tuning: 1.2M API req/s on a 4 vCPU EC2 Instance](https://talawah.io/blog/extreme-http-performance-tuning-one-point-two-million/)
    * [Flame Graphs](https://www.brendangregg.com/flamegraphs.html)
    * [wrk - a HTTP benchmarking tool](https://github.com/wg/wrk)

## Prerequisites

* Linux host such as Arch Linux, Debian, Ubuntu, RHEL ...etc
* Python >= 3.10
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programming_languages/python/python.md#usage-with-pyenvpoetry)
    * pyenv for Python versions control
    * poetry for Project dependency control
    * Project dependcy detialls will be in pyproject.toml/poetry.lock
* PostgreSQL == 15.3 or Django builtin SQLite
    * [PostgreSQL 15.4 Documentation](https://www.postgresql.org/docs/15/index.html)
    * [PostgreSQL with docker](https://hub.docker.com/_/postgres)
    * [pacman directly install PostgreSQL on Arch Linux](https://wiki.archlinux.org/title/PostgreSQL)
* tree
    * a CLI tools to list contents of directories in a tree-like format.
* docker/podman (just pickup one to do conatiner image building and running)
* kind for create local Kubernetes clusters via docker/podman

## Quick Start

```shell
#spawns a virtual environment
poetry shell

#add packages
#src: https://python-poetry.org/docs/cli/#add
poetry add django

#remove packages
poetry remove diagrams

#for help
python3 manage.py help

#Creating a superuser for Django CMS system
python3 manage.py createsuperuser

#run devserver
python3 manage.py runserver

#src: https://docs.python.org/3.8/library/sys.html#sys.path
#A list of strings that specifies the search path for modules. 
#Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
python -c "import sys; print(sys.path)"

#add env PYTHONPATH
export PYTHONPATH=/path/to/your/module:$PYTHONPATH

#add packages by poetry
poetry add "psycopg[binary,pool]"
poetry add django-environ

#add packages by poetry to extras section
poetry add diagrams --optional --extras diagrams

#export requirements.txt if needed
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --output requirements.txt --without-hashes

#podman comon operations
#login container registry such docker hub
podman login docker.io
podman images
podman container list --all
podman container rm local_library
podman rmi localhost/dev-test:latest

#docker/podman build container image
#docker build -t dev-test -f Dockerfile.dev
podman build --no-cache -t local_library_website/dev-test -f Dockerfile.dev
podman build -t docker.io/focal1119/local_library_website:dev -f Dockerfile.dev

#prod build
podman build -t docker.io/focal1119/local_library_website:prod -f Dockerfile.prod
podman build --no-cache -t docker.io/focal1119/local_library_website:prod -f Dockerfile.prod

#test docekr/podman container image in localhost when PostgreSQL is online
podman run -d --env-file=.env --name local_library -p 8000:8000 localhost/dev-test

#run with Dockerfile.dev
podman run -d --env-file=.env --name local_library -p 8000:8000 docker.io/focal1119/local_library_website:dev

#run with Dockerfile.prod
podman run -d --env-file=.env --name local_library -p 8000:8000 docker.io/focal1119/local_library_website:prod

#check logs
podman logs --follow local_library

#push
# docker push docker.io/focal1119/local_library_website:tagname
docker push docker.io/focal1119/local_library_website:dev
podman push docker.io/focal1119/local_library_website:dev
podman push docker.io/focal1119/local_library_website:prod

#pull
docker pull focal1119/local_library_website:dev

#.env.example for using and doing modification for your usecase
vim .env.example
```
