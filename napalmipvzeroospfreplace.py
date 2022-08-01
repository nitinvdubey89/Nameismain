"""
Author: IpvZero

"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import napalm_configure
from nornir_utils.plugins.functions import print_result
from napalmreplaceregex import replace_ospf

nr = InitNornir(config_file="config.yaml")

def replace_feature(task):
    config = replace_ospf(task)
    task.run(task=napalm_configure,configuration = config, replace=True)

result = task.run(task=replace_feature)
print_result(result)
