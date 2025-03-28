# Module 5 - Docker Compose

**Goal**: Learn how Docker Compose

## Steps

1. Examine the following files:

- `Dockerfile`
- `docker-compose.yml`
- `app.py`

2. This time we'll use docker compose to build and run two containers: `app.py` and `redis`

  ```shell
  docker compose up --build
  ```

3. After build is complete and both containers are online, navigate to localhost:4000 to see the application running
4. Run `docker ps` to see what's happening
5. Run `docker compose down` to stop the containers
6. Run `docker compose rm` to delete the stopped containers
