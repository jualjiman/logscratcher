from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_lenght=100, help_text="Nombre del proyecto")
	path = models.CharField(max_lenght=300, help_text="Ruta del proyecto")
	