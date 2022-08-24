from django.db import models
from django.contrib.auth.models import User

class FileModel(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    file = models.FileField(User, upload_to='documents/')
    revision = models.IntegerField()
