# Docker build images workflow in Python

Since docker hub stopped building images for free accounts, I've been looking for another way to do it.
I could have used simple shell scripts, but that's too simple and not fun. 
So I found a way to continue playing with Python by using a library I heard about a few weeks ago.

## Using Spotify luigi and docker-py libraries to build docker images

Remember, it's just a way to explore and use library like Spotify luigi or docker-py.

# Docker images structure

    [image]/[sub]/Dockerfile

Sub directory is optional.

    [image]/Dockerfile

## Run tasks command

Start the docker-compose of the project, 

    docker compose up -d

go inside the python container,

    docker compose exec python bash

Inside the project python environment,

    poetry shell

Build PHP 8.2 images, and push it to Docker repository.

    # Fpm image
    python -m luigi --module task_php_images Push --version 8.2 --sub fpm --date '2023-09-29'

    # Dev image
    python -m luigi --module task_php_images Push --version 8.2 --sub dev --date '2023-09-29'

    # Cli image
    python -m luigi --module task_php_images Push --version 8.2 ---sub cli --date '2023-09-29'


Build the Python 3.11 image, and push it to Docker repository.

    python -m luigi --module task_python_images Push --version 3.11 --date '2023-09-29'

Build the PostgreSQL 15 image from TimescaleDB with Replibyte tool, and push it to Docker repository.

    python -m luigi --module task_db_images Push --version pg.15 --date '2023-09-29'


Push task has a dependency task, the Build task. Before running the Push task luigi executes the Build task.