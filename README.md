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

Build PHP 7.4 image, and push it to Docker repository.

    python -m luigi --module task_php_image PushImage --version 7.4 --date '2021-12-18'

    # Dev image
    python -m luigi --module task_php_image PushImage --version 7.4 -sub dev --date '2021-12-18'

    # Cli iaage
    python -m luigi --module task_php_image PushImage --version 7.4 -sub cli --date '2021-12-18'


Build the Python 3.10 image, and push it to Docker repository.

    python -m luigi --module task_python_image PushImage --version 7.4 --date '2021-12-18'