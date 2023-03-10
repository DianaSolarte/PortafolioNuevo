from django.db import models

class Ability(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ='skill/images/')
