# first check the config is pressent and then apply

# netmiko will alwayts push but napalm

# napalm is used for idempotency

# REST CONFIG

# PUT
# OPERATTION REQUEst
# napalm will mention desired state and whatever is not in the desired state will automaticlly be removed

# NAPALM REPLACE
# NAPALM VALIDATE : TESTING TOOL
# GETTERS
#NAPALM BACKUPS
###################################################################################

#NAPALM BACKUUP (using nornri)
#DEVICE PREPARATION
#REPLACE
########################################################################

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import  write_file
import pathlib # create files path

nr = InitNornir(config_file="config.yaml")

config_dir = "backup-directory"
config_dir_startup = "backup-startup"
def backup_configuration(task):
    config_result = task.run(task=napalm_get,getters=["config"])
    startup_config = config_result.result["config"]["startup "] # result is the attribut to get dictionary output
    running_config = config_result.result["config"]["running "] # result is the attribut to get dictionary output
    print(running_config) # this gives the running config in string type
    # we will create a folder called backups and within that folder we will write the config.txt
    pathlib.Path(config_dir).mkdir(exist_ok=True) #check whether directr=ory already exisits
    task.run(task=write_file,content=running_config,filename =f"backup-directory/{task.host}.")
    task.run(task=write_file,content=running_config,filename =f"backup-startup/{task.host}.")



results = nr.run(task=backup_configuration)
print_result(results)