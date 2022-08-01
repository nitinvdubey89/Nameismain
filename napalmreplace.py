from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result


nr  = InitNornir(config_file="config.yaml")


def replace_stuff(task):
    task.run(task=napalm_configure, filname=f"backup-directory/{task.host}.txt", replace=True)

results=nr.run(task=replace_stuff)
print_result(results)
############ DRY RUN##############################

### NAPALM DEFAULT BEHAVIOUR IS TO MERGE THE CONFIGURATION###########

###### BANNER MOTD ######################

### BANNER use the EXT CHAR(ASCII 3) . This looks like a cntl-c in nthe file but as a single character,
# press ctrl+v and then release v and press C
#

















