from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./template")

devices = [
    {
        "hostname": "nxos1",
        "intf1": "Ethernet1/1",
        "intf1_ip": "10.1.100.1",
        "intf1_mask": "24",
        "peer1_ip": "10.1.100.2",
    },
    {
        "hostname": "nxos2",
        "intf1": "Ethernet1/1",
        "intf1_ip": "10.1.100.2",
        "intf1_mask": "24",
        "peer1_ip": "10.1.100.1",
    },
]

for template_vars in devices:
    template_file = 'nxos_template.j2'
    template = env.get_template(template_file)
    output = template.render(**template_vars)
    print(output)
    #break
