# Module 5 - Docker Run

**Goal**: Learn to pull and run public docker images

## Steps

1. Ensure Docker CLI installed: `docker --version`
2. Pull an image: `docker pull hello-world`
3. Check that the image is on the local cache: `docker images`
4. Run the image: `docker run -it hello-world`
5. Run an ubuntu image interactively: `docker run -it ubuntu:noble bash`

- You are now inside the running container, you may run any command you want
- Install curl: `apt-get update && apt-get install curl`
- Try curl: `curl google.com`
- Exit the container: `CTRL+C`

6. View terminated containers: `docker ps -a`
7. Run the ubuntu container again: `docker run -it ubuntu:noble bash`

- Try to execute curl again: `curl google.com`
- The changes you made on the last container are lost
