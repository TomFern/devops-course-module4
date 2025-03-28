# Module 5 - Docker CLI commands

**Goal**: Learn most common CLI commands

## Steps

Run the following commands and observe the output.

### docker exec

Attach a session on a running container

```shell
# start a docker container
$ docker run -it -p 4000:4000 myapp 

# open a second terminal, observe the container ID, for example

$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                              NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Up 4 seconds   0.0.0.0:4000->4000/tcp, 5000/tcp   xenodochial_leavitt

# connect to the running container
$ docker exec -it f81f4329c105 bash

# you are inside the container, inspect what processes are running
$ ps -ef

# try killing the app.py process, which usually is ps id 1
$ kill 1

# Killing the process that started with the container stops the container
# you should now be outside the container and the container should be stopped
```

### docker start/stop

This command allows you to pause and resume a container without killing it.

```shell
# start a docker container
$ docker run -it -p 4000:4000 myapp 

# open a second terminal, observe the container ID, for example

$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                              NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Up 4 seconds   0.0.0.0:4000->4000/tcp, 5000/tcp   xenodochial_leavitt

# stop the container using its ID
$ docker stop f81f4329c105

# the container is paused, confirm with docker ps, it should return an empty list
$ docker ps

# resume the container
$ docker start f81f4329c105

# run docker ps to see the container running again, this is the same container as before
$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                              NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Up 4 seconds   0.0.0.0:4000->4000/tcp, 5000/tcp   xenodochial_leavitt
```

### docker logs

View the logs of a container

```
# view the docker container id with docker ps
$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                              NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Up 4 seconds   0.0.0.0:4000->4000/tcp, 5000/tcp   xenodochial_leavitt

# run docker logs to the the output of the commands running in the container
$ docker logs f81f4329c105
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:4000
 * Running on http://172.17.0.2:4000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 253-451-794
```

### docker rm

Stopped containers remain in the system, taking disk space. You can completely remove them with `docker rm`

```shell
# see the running containers
$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                              NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Up 4 seconds   0.0.0.0:4000->4000/tcp, 5000/tcp   xenodochial_leavitt

# stop the container
$ docker stop f81f4329c105

# view the stopped containers
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS                      PORTS        NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Exited (0) 12 minutes ago                xenodochial_leavitt

# remove the container
$ docker rm f81f4329c105

# the container should no longer appear, even as stopped
$ docker ps -a
```

### docker inspect

```shell
# start a docker container
$ docker run -it -p 4000:4000 myapp 

# see the container id on a second terminal
$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS                      PORTS        NAMES
f81f4329c105   test      "python app.py"   4 seconds ago   Exited (0) 12 minutes ago                xenodochial_leavitt

# run docker inspect to learn about the container metadata
# docker inspect f81f4329c105
[
    {
        "Id": "a5e587aa0a2f36621ce5dadb2cecb741b692adc8eb8a636512e588071ef4d474",
        "Created": "2025-03-28T15:10:41.117254219Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1284,
            "ExitCode": 0,
...
```

Analyze what data is available in the JSON object returned by Docker inspect.
