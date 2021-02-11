from django.db import models


# Create your models here.


class Student_store_model(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.EmailField()
    Department = models.CharField(max_length=60)

    def __str__(self):
        return self.Name
