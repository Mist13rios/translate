For local server start:

1). Install docker

2). Change current folder on project_dir
Here I use docker-compose, for it in current directory you need docker-compose.yml as instruction file.

3). Run 'docker-compose build'
It's will be take a time, docker download files for build and install new docker image

4). Run 'docker-compose up app_parse'
It's will be start current working container, that version use only 1 docker container,
without encapsulating db/nginx/app envs.

After it you can see server local, on http://127.0.0.1:8000 or with your docker net ip .

Current project use 8000 port.
