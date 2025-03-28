# Module 5 - Docker Build

**Goal**: Learn how to build docker images

## Steps

1. Examine the `Dockerfile`, try to understand what each line docker
2. The `app.py` and `requirements.txt` are duplicate files from the ones used in Module 4
3. Build a docker image: `docker build -t myapp .`
4. Run the docker image: `docker run -it -p 4000:4000: myapp`
5. Open a browser on localhost:4000, you should see the application running
6. Press `CTRL+c` in the terminal to stop the container
7. Run an interactive session to access the containers: `docker run -it myapp bash`
8. You are now inside the container, you can run `ls` to see the files in the container. Do you see any files that shouldn't be there?
9. Exit the session by pressing `CTRL+d`
10. Create a file called `.dockerignore` and add the following like `Dockerfile`
11. Run steps 3 to 9 again, this time the `Dockerfile` should not be in the container
