from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
from jinja2 import Template

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

bgp_config = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
    address-family ipv4 unicast
"""

j2_template = Template(bgp_config)
output = j2_template.render(local_as=10, peer1_ip="10.1.20.2", peer1_as=20, peer2_ip="10.1.30.2", peer2_as=30,)
print(output)