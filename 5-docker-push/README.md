# Module 5 - Docker Registries

**Goal**: Learn how to store and share images using registries

## Steps

1. Create or login to an account on <https://hub.docker.com>
2. Execute `docker login`, you may be prompted to enter your Docker Hub username and password
3. Before uploading an image, you must rename it with your Docker Hub username, for example: `docker tag myapp tomfern/myapp:latest`
4. Now push the image to Docker Hub: `docker push tomfern/myapp:latest`
5. Now other people can pull your image to their machines with: `docker pull tomfern/myapp:latest`. Try sharing images between your classmates!
