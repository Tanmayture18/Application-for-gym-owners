from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()


    def __str__(self):
        return self.name
    