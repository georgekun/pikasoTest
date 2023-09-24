# Используйте официальный образ Python в качестве базового образа
FROM python:3.8
RUN apt-get update && apt-get install -y supervisor

# Установите переменную окружения для отключения вывода буферизации Python
ENV PYTHONUNBUFFERED 1


# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app/

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Запустите Django приложение
RUN  echo "Сборка завершен"
CMD ["supervisord", "-c", "/app/supervisord.conf"]