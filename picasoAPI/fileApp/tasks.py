import time

from picasoAPI.celery import app
from .models import File


@app.task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)

        
        print(f'идет обработка файла с индексом [{file_id}]...PROCCESSED = {file.proceesed}')
        # Ваш код для обработки файла здесь
        # Пример: Изменение поля processed на True
        time.sleep(20)
        file.proceesed = True
        file.save()
        print(f'обработка файла с индексом [{file_id}] готова...PROCCESSED = {file.proceesed}')
    except File.DoesNotExist:
        print("не сохранилось")