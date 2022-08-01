# if changes fail then we should be able to rollback to previous configration
# archive
#file operations , scp should be enabled for all routers to implement archive feature
# ip scp server enable
# arhcive
# path flash:archive
#write-memeory
# using nornir_scrapli to push textfile to all devices

# send_configs_from_file.py

from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test(task):
    task.run(task=send_configs_from_file, file="napalm-startup.txt")

results = nr.run(task=test)
print_result(results)
