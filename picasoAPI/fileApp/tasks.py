import time

from picasoAPI.celery import app
from .models import File


@app.task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)        
        # Ваш код для обработки файла здесь, я для примера просто задержку поставил
        time.sleep(20)
        file.proceesed = True
        file.save()
    except File.DoesNotExist:
        print("не сохранилось")