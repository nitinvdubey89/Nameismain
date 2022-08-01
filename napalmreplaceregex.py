import logging
import re
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

etx = chr(3)

def replace_ospf(task):
    data = task.run(
        task = load_yaml,
        file = f"./host_vars/{task.host}.yaml",
        severity_level=logging.DEBUG,
    )
    task.host["facts"]= data.result
    config = task.run(task=napalm_get, getters=["config"], severity_level=logging.DEBUG)
    showrun= config.result["config"]["running"]
    pattern = re.compile("^router ospf([^!])+",flags=re.I | re.M)
    routing_template = task.run(
        task=template_file,
        name = "Building Routing Configuration",
        template = "ospfreplace.j2",
        path ="./templates",
        severity_level = logging.DEBUG,
    )
    template_to_load = routing_template.result
    newconfig = re.sub(pattern, template_to_load, showrun)
    final_config = newconfig.replace("^C", etx)
    return final_config



