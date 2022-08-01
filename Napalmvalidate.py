import logging
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_validate
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr  = InitNornir(config_file="config.yaml")

def get_test(task):
    task.run(task=napalm_get, getters=["get_facts"])


def validate_test(task):
   result= task.run(task=napalm_validate, src=f"validate-{tassk.host}.yaml", severity_level=logging.DEBUG)
   task.host["facts"] = result.result
   assessment = task.host["facts"]["complies"]
   if assessment == True:
       message = "PASS"
   else:
        message = task.host["facts"]
   return   Result(host=task.host, result=message)

######compares with validation file####################################
result = nr.run(task=validate_test)
print_result(result)


results = nr.run(task=get_test)
print_result(results)

###### HERE WE WILL GET JSON OOUTPUT FROM THE FACTS AND WE NEED TO CONVERT IT TO YAML #######
#############################################################################################

