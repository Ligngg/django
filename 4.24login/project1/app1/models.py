from django.db import models

# Create your models here.

class task1django(models.Model):
    name=models.CharField(max_length=60)
    img=models.ImageField(upload_to="pics")
    desp=models.TextField()

    def __str__(self):
        return self.name


