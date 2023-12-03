from django.db import models

# Create your models here.


class Database(models.Model):
    file = models.FileField(
        upload_to="File/", max_length=500, null=True, default=None)