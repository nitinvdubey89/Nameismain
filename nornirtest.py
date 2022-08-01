from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs_from_file

from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands = input("\Enter commands you wish to send: ")
cmds = commands.split(",")


def push_show_commands(task):
    for cmd in cmds:
        task.run(task = send_command,command = cmd)

results = nr.run(task=push_show_commands)
print_result(results)


def push_configs(task):
    task.run(task=send_configs_from_file, file ="testconfig.txt")

results = nr.run(task=push_configs)
print_result(results)