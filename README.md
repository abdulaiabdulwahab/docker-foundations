# docker-foundations.
# Docker Foundations Project

This project is a simple hands-on introduction to Docker. It demonstrates how to containerize a basic Python Flask application, build a Docker image, run a container, expose ports, use environment variables, inspect logs, and persist data with Docker volumes.

## Project Goals

The goal of this project is to understand the core Docker workflow:

```text
Source Code
   ↓
Dockerfile
   ↓
docker build
   ↓
Docker Image
   ↓
docker run
   ↓
Docker Container
```

## Technologies Used

- Docker
- Python
- Flask
- PowerShell

## Project Structure

```text
docker-foundations/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Docker Concepts Practiced

This project covers:

- Docker images
- Docker containers
- Dockerfiles
- Image layers
- Port mapping
- Environment variables
- Container logs
- Docker Exec
- Docker Inspect
- Docker volumes
- Persistent storage
- Basic Docker troubleshooting

## Build the Docker Image

From the project directory, run:

```powershell
docker build -t docker-foundations:v1 .
```

Verify the image:

```powershell
docker images
```

## Run the Container

Run the application and map port `8080` on the host to port `5000` inside the container:

```powershell
docker run -d `
  --name foundations-api `
  -p 8080:5000 `
  docker-foundations:v1
```

Open the application at:

```text
http://localhost:8080
```

Or test it with:

```powershell
curl.exe http://localhost:8080
```

## View Running Containers

```powershell
docker ps
```

View all containers:

```powershell
docker ps -a
```

## View Container Logs

```powershell
docker logs foundations-api
```

Follow logs in real time:

```powershell
docker logs -f foundations-api
```

## Access the Container

Open a shell inside the running container:

```powershell
docker exec -it foundations-api sh
```

Useful commands inside the container:

```sh
pwd
ls -la
python --version
```

Exit the container:

```sh
exit
```

## Use Environment Variables

Stop and remove the current container:

```powershell
docker stop foundations-api
docker rm foundations-api
```

Run the container with a custom environment variable:

```powershell
docker run -d `
  --name foundations-api `
  -p 8080:5000 `
  -e APP_MESSAGE="Learning Docker!" `
  docker-foundations:v1
```

Test:

```powershell
curl.exe http://localhost:8080
```

## Persistent Storage with Docker Volumes

Create a Docker volume:

```powershell
docker volume create foundations-data
```

Run the container using the volume:

```powershell
docker run -d `
  --name foundations-api `
  -p 8080:5000 `
  -v foundations-data:/data `
  docker-foundations:v1
```

View available volumes:

```powershell
docker volume ls
```

Inspect the volume:

```powershell
docker volume inspect foundations-data
```

The volume allows application data to remain available even if the container is deleted and recreated.

## Useful Docker Commands

```powershell
docker build -t docker-foundations:v1 .
docker images
docker ps
docker ps -a
docker logs foundations-api
docker exec -it foundations-api sh
docker inspect foundations-api
docker stop foundations-api
docker rm foundations-api
docker volume ls
```

## Troubleshooting

If the container stops unexpectedly:

```powershell
docker ps -a
docker logs foundations-api
```

If port `8080` is already being used, choose another port:

```powershell
docker run -d `
  --name foundations-api `
  -p 8081:5000 `
  docker-foundations:v1
```

Then access:

```text
http://localhost:8081
```

If Docker appears to be using an old build:

```powershell
docker build --no-cache -t docker-foundations:v2 .
```

## What I Learned

Through this project I practiced how to:

- Create a Dockerfile
- Build Docker images
- Create and manage containers
- Publish container ports
- Configure containers with environment variables
- Inspect container logs
- Execute commands inside containers
- Troubleshoot failed containers
- Persist application data using Docker volumes

