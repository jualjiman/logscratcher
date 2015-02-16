 # -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Server(models.Model):
	name = models.CharField(max_length=20, help_text="Server Name")
	user = models.CharField(max_length=30, help_text="Server user")
	host = models.CharField(max_length=30, help_text="Server host")
	password = models.CharField(max_length=30, blank=True, help_text="Server pass for user, not needed if you're in authoriced_keys ")
	description = models.CharField(max_length="600", blank=True, help_text="Some server notes")

	def __str__(self):
		return self.name
class WhereIs(models.Model):
	name = models.CharField(max_length=30,help_text='Where is name')

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=100, help_text="Project Name")
	path = models.CharField(max_length=300, help_text="Project Path")
	status = models.CharField(blank=True,editable=False, max_length=30, help_text="Project status")
	last_update = models.DateTimeField(blank=True,null=True, editable=False)
	server = models.ForeignKey(Server,help_text="where to scratch log")
	whereIs = models.ForeignKey(WhereIs, blank=True, help_text="where are files to back up")
	active = models.BooleanField()
	
	def __str__(self):
		return self.name
