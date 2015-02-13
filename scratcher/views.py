 # -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import envoy, re
from datetime import datetime

# Create your views here.

def execute_command(command,timeout=330):
	fabric_command = str(command)
	print command
	r = envoy.run(fabric_command, timeout=timeout)
	return r

def update_project(pid):
	project = Project.objects.get(id=pid)
	#server = execute_command("fab define_server:'%s','%s'" % (project.server.name, project.server.data))
	#command = "fab -H %s -u %s -p %s scratch_logs:path='%s'" % (project.server.host, project.server.user, project.server.password, project.path,)
	command = "bash run.sh %s %s '%s'" % (project.server.user, project.server.host, project.path,)

	out = execute_command(command).std_out
	start = "*#Terminado"
	end = "#*"
	last_update = out[out.find(start)+len(start):out.rfind(end)].strip()

	# *#Terminado 2015-08-16 11:42:00#*
	if not last_update == '':
		#last_datetime = datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S')

		#2015-08-16 11:42:00
		p = re.compile('[:\s-]')
		datep = map(int, p.split(last_update))
		
		last_datetime = datetime(datep[0],datep[1],datep[2],datep[3],datep[4],datep[5])
		project.last_update = last_datetime
		project.status = "Done"
	else:
		project.status = "Error"

	project.save()

	return project

def getting_log_data(pid):
	project = update_project(pid)
	return project.last_update.strftime('%b. %d, %Y, %I:%M:%S %p') + "-" + project.status

@csrf_exempt
def refresh_log_data(request, pid):
	return HttpResponse(getting_log_data(pid))


def home(request):
	projects = list(Project.objects.filter(active=True))

	for indx, project in enumerate(projects):
		projects[indx] = update_project(project.id)

	return render(
		request,
		"projects.html",
		{
			"projects" : projects,
		} 
	)