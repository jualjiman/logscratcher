from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','path','last_update','server','whereIs','active',)

class ServertAdmin(admin.ModelAdmin):
	list_display = ('name','user','host','description',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(WhereIs)
admin.site.register(Server, ServertAdmin)