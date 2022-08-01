from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from pytest_check import check_func

nr = InitNornir(config_file="config.yaml")
#With InitNornir you can initialize nornir with a configuration file, with code or with a combination of both.
#Now that you know how to initialize nornir and work with the inventory let’s see how we can leverage it to run tasks on groups of hosts.

#A task is a reusable piece of code that implements some functionality for a single host. In python terms it is a function that takes a Task as first paramater and returns a Result.
def loadvars(task):
    result = task.run(task=load_yaml, file=f"desired-stat/vlans/{task.host}.yamml")
    loaded = result.result
    return loaded

@check_func
def pullospf(task):
    vlan_list = []
    result = task.run(task=send_command, command="show ip ospf neighbor ")
    task.host["facts"] = result.scrapli_response.genie_parse_output()
    vlans = task.host["facts"]["vlans"]
    for vlan in vlans:
        if vlan in ["1", "1002", "1003", "1004", "1005"]:
            continue
        vlan_id = int(vlan)
        name = vlans[vlan]["name"]
        vlan_dict  = {"id": vlan_id, "name": name}
        vlan_list.append(vlan_dict)
    expected = load_vars(task)
    assert expected == vlan_list, f"{task.host} FAILED"

    print(vlan_list)
    print("\n\n")

def test_nornir(nr):
    nr.run(task=pullospf )
#nr.run(task=pullospf)
#@import ipdb
#ipdb.set_trace()
