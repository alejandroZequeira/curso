# Guía de Uso de Docker

Este documento proporciona ejemplos básicos para manejar redes, volúmenes y desplegar imágenes de contenedores en Docker.

## 1. Ejemplo de Manejo de Redes

### Crear una red:
```bash
docker network create -d bridge <name_network> --subnet=10.0.0.1/25
```
### Para listar redes:
```bash
docker  network  ls
```
### Para inspeccionar una red:
```bash
docker  network inspect <id_network> 
```
### Para eliminar una red por ID:
```bash
docker  network rm <id_network> 
```
### Para eliminar una red por nombre:
```bash
docker  network rm <name_network> 
```

## 2.-Ejemplo de manejo de volúmenes.

### Crear un volumen: 
```bash
docker volume create <volumen_name>
```
### Listar volúmenes:
```bash
docker  volume ls
```
### Inspeccionar un volumen:
```bash
docker  volume inspect <volumen_name> 
```
### Eliminar un volumen:
```bash
docker  volume rm <volumen_name>
```

## 3.-Ejemplo de despliegue de imágenes de contendor.

### Crear y ejecutar un contenedor:
```bash
docker run -d --name <container_name> <image_name>
```
### Listar contenedores en ejecución:
```bash
docker ps
```
### Listar todos los contenedores (incluidos los detenidos):
```bash
docker ps -a
```
### Inspeccionar un contenedor:
```bash
docker inspect <container_id>
```
### Detener un contenedor:
```bash
docker stop <container_id>
```
### Iniciar un contenedor detenido:
```bash
docker start <container_id>
```
### Reiniciar un contenedor:
```bash
docker restart <container_id>
```
### Eliminar un contenedor detenido:
```bash
docker rm <container_id>
```
### Descargar una imagen desde un repositorio (por ejemplo, Docker Hub):
```bash
docker pull <image_name>
```
### Ver los registros (logs) de un contenedor:
```bash
docker logs <container_id>
```
### Acceder al shell bash de un contenedor en ejecución:
```bash
docker exec -it <container_id> /bin/bash
```

## 4.-Comandos para Docker Compose

### Crear y ejecutar contenedores basados en un archivo docker-compose.yml:
```bash
docker-compose up
```
### Crear y ejecutar contenedores en segundo plano (modo "detached"):
```bash
docker-compose up -d
```
### Detener los contenedores en ejecución:
```bash
docker-compose stop
```
### Detener y eliminar los contenedores, redes y volúmenes creados por docker-compose:
```bash
docker-compose down
```
### Listar los contenedores gestionados por docker-compose:
```bash
docker-compose ps
```
### Ver los logs de los servicios definidos en docker-compose:
```bash
docker-compose logs
```
### Ver los logs de un servicio específico:
```bash
docker-compose logs <service_name>
```
### Escalar el número de contenedores de un servicio:
```bash
docker-compose up -d --scale <service_name>=<num_instances>
```
### Ejecutar un comando dentro de un contenedor gestionado por docker-compose:
```bash
docker-compose exec <service_name> <command>
```
### Reconstruir las imágenes de los servicios:
```bash
docker-compose build
```
### Reconstruir y reiniciar los contenedores:
```bash
docker-compose up --build
```

## 5.-Comandos para Limitar Recursos en Docker y Docker Compose

### Limitar Recursos de Contenedores con Docker

### Limitar el uso de CPU:
```bash
docker run --cpus="<num_cpus>" <image_name>
Ejemplo: docker run --cpus="1.5" ubuntu
```
### Limitar la memoria:
```bash
docker run --memory="<memory_limit>" <image_name>
Ejemplo: docker run --memory="512m" ubuntu
```
### Establecer límites de intercambio de memoria (swap):
```bash
docker run --memory-swap="<swap_limit>" <image_name>
Ejemplo: docker run --memory="512m" --memory-swap="1g" ubuntu
```
### Limitar el peso de E/S en disco (I/O):
```bash
docker run --blkio-weight="<weight>" <image_name>
Ejemplo: docker run --blkio-weight="500" ubuntu
```
---

## 6.-Limitar Recursos en Docker Compose

### Para limitar recursos usando `docker-compose`, añade las configuraciones al archivo docker-compose.yml:
```bash
version: '3.7'

services:
  app:
    image: <image_name>
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: "256M"
        reservations:
          cpus: "0.25"
          memory: "128M"
```

### Limitar CPU:
```bash
- limits.cpus: Limita el número de núcleos de CPU disponibles para el servicio.
Ejemplo: cpus: "0.5" (medio núcleo).
```
### Limitar memoria:
```bash
- limits.memory: Establece el límite máximo de memoria.
Ejemplo: memory: "256M" (256 MB).
```
### Reservar recursos:
```bash
- reservations: Permite reservar una cantidad mínima de recursos para un servicio.
Ejemplo: cpus: "0.25" y memory: "128M".
```