#!/usr/bin/env bash
cd .. && docker run -it --rm -v $(pwd):/var/www --net=myprod_dev -u $UID:$GID --env-file .env myprod/py:3.10 bash