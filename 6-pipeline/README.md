# Module 5 - Build and push docker image using CI/CD pipeline

**Goal**: Learn to build images in CI pipeline

## Steps

1. Create a **project** secret with your Docker credentials

- DOCKER_USERNAME
- DOCKER_PASSWORD

2. Setup a pipeline that builds and pushes the image to Docker Hub (you need to import the secret and login to Docker Hub)
3. Bonus points if you can use Docker layers to speed up the build process

## Tips

- You can uniquely identify every build using one of these environment variables: `SEMAPHORE_WORKFLOW_ID`, or `SEMAPHORE_GIT_SHA`
- For this pipeline use the agent `s1-ubuntu`
- Check pipeline.png in this folder to see an example.
- The `solution` branch contains a working pipeline
- You need to create
