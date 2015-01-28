 # -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Server(models.Model):
	name = models.CharField(max_length=20, help_text="Server Name")
	user = models.CharField(max_length=30, help_text="Server user")
	host = models.CharField(max_length=30, help_text="Server host")
	password = models.CharField(max_length=30, help_text="Server pass for user, not needed if you're in authoriced_keys ")
	description = models.CharField(max_length="600", help_text="Some server notes")

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(blank=True, max_length=100, help_text="Project Name")
	path = models.CharField(blank=True, max_length=300, help_text="Project Path")
	status = models.CharField(blank=True,editable=False, max_length=30, help_text="Project status")
	last_update = models.DateTimeField(blank=True,null=True, help_text='Fecha y hora de inicio de la publicacion')
	server = models.ForeignKey(Server)
	
	def __str__(self):
		return self.name