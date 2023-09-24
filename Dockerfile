# Используйте официальный образ Python в качестве базового образа
FROM python:3.8
RUN apt-get update && apt-get install -y supervisor

# Установите переменную окружения для отключения вывода буферизации Python
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Склонируйте репозиторий GitHub внутри контейнера
RUN git clone https://github.com/yourusername/yourrepository.git .

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Запустите Django приложение
RUN  echo "Сборка завершена"
CMD ["supervisord", "-c", "/app/supervisord.conf"]