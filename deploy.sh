#!/bin/bash
# Остановка и удаление контейнеров
docker-compose down
# Пересборка и запуск контейнеров в фоновом режиме
docker-compose up -d --build
