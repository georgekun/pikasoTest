from django.db import models
from django.utils import timezone

class File(models.Model):
	id = models.AutoField(primary_key = True)
	file = models.FileField(upload_to="files/")
	uploaded_at = models.DateTimeField(default = timezone.now)
	proceesed = models.BooleanField(default = False)