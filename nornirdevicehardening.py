from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs_from_file
import ipdb

from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    version_result  = task.run(task=send_command, command="show version")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    print(task.host["facts"])

results = nr.run(task=pull_structured_data)
#print_result(result)
ipdb.set_trace()
