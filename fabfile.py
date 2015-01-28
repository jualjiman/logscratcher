from fabric.api import  *
from fabric.colors import green,red
from fabric.api import env

env.roledefs = {} 

# env.roledefs = {
#'hitman': ['wadmin@191.101.13.47'],
#}

# @task
# def define_server(name, data):
# 	"""
# 		define a server
# 	"""
# 	if not name in env.roledefs:
# 		env.roledefs[name] = [data,]

# @task
# def imprimir():
# 	print env.roledefs

@task
def scratch_logs(path):
    """
        scratch given logs looking for last update date
    """
    run("cat %s | grep -iA0 'Terminado' --color | tail -n 1" % (path,))

