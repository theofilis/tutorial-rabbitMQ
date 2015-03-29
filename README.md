## RabbitMQ Dockerfile


This repository contains **Dockerfile** of [RabbitMQ](http://www.rabbitmq.com/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/rabbitmq/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/ubuntu](http://dockerfile.github.io/#/ubuntu)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/rabbitmq/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/rabbitmq`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/rabbitmq" github.com/dockerfile/rabbitmq`)

### REPO
1. https://github.com/rabbitmq/rabbitmq-server
2. https://github.com/rabbitmq/rabbitmq-tutorials

### Usage

#### Run `rabbitmq-server`

    docker run --name rabbitmq -d -p 5672:5672 -p 15672:15672 dockerfile/rabbitmq

#### Run `rabbitmq-server` w/ persistent shared directories.

    docker run --name rabbitmq -d -p 5672:5672 -p 15672:15672 -v <log-dir>:/data/log -v <data-dir>:/data/mnesia dockerfile/rabbitmq

### Books
1. RabbitMQ in Action
2. RabbitMQ Essentials
3. RabbitMQ Cookbook (Packt Publishing)
4. RabbitMQ Cookbook (Safari Online)

