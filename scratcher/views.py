 # -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import envoy
from datetime import datetime

# Create your views here.

def execute_fabric_command(command,timeout=30):
	fabric_command = str(command)
	r = envoy.run(fabric_command, timeout=timeout)
	return r.std_out

def update_project(pid):
	project = Project.objects.get(id=pid)

	#server = execute_fabric_command("fab define_server:'%s','%s'" % (project.server.name, project.server.data))
	command = "fab -H %s -u %s -p %s scratch_logs:path='%s'" % (project.server.host, project.server.user, project.server.password, project.path,)
	out = execute_fabric_command(command)
	print out
	start = "*#Terminado"
	end = "#*"
	last_update = out[out.find(start)+len(start):out.rfind(end)].strip()

	# *#Terminado 2015-08-16 11:42:00#*
	last_datetime = datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S')
	project.last_update = last_datetime
	project.save()

	return project

def getting_log_data(pid):
	return update_project(pid).last_update.strftime('%b. %d, %Y, %I:%M:%S %p')

@csrf_exempt
def refresh_log_data(request, pid):
	return HttpResponse(getting_log_data(pid))

def home(request):
	projects = list(Project.objects.all())

	for indx, project in enumerate(projects):
		projects[indx] = update_project(project.id)

	return render(
		request,
		"projects.html",
		{
			"projects" : projects,
		} 
	)