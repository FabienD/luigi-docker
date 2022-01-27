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

Inside docker container : 

    docker-compose exec python bash

Inside the project python environment,

    poetry shell


Build PHP 8.1 image, and push it to Docker repository.
    
    # Fpm image
    python -m luigi --module task_php_images Push --version 8.1 --sub fpm --date '2021-12-18'

    # Dev image
    python -m luigi --module task_php_images Push --version 8.1 -sub dev --date '2021-12-18'

    # Cli image
    python -m luigi --module task_php_images Push --version 8.1 -sub cli --date '2021-12-18'


Build the Python 3.10 image, and push it to Docker repository.

    python -m luigi --module task_python_image Push --version 3.10 --date '2021-12-18'

Push task has a dependency task, the Build task. Before running the Push task luigi executes the Build task.