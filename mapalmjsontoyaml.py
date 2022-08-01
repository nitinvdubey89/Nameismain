import yaml
import json
from pprint import pprint

target_dict = json.dump(friends.json)

filename = "validate-R1.yaml"
with open(filename, "w" ) as f:
    output = yaml.dump(target_dict, f , default_flow_style=False)