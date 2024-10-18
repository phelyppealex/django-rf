from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    cargo = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
