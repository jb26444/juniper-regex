import json
import pprint
import re


# En\w+ - Enable whole word
# ge-\d\/\d\/\d - ge
#int_dic.update({'Name': name})
#state_dic.update({'State': state})
#state_dic.update({'link': link})
#int_dic.update(state_dic)
#(' '.join(fruits)) - remove square brackets

text = """const text = `
Physical interface: ge-0/0/0, Enabled, Physical link is Up
  Interface index: 138, SNMP ifIndex: 506, Generation: 141
  Description: STATIC1R16
  Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps, BPDU Error: None,"""

#t = re.findall(reg, text)
reg = "ge-\d\/\d\/\d"
reg1 = "En\w+"
reg2 = "Up"
int_dic = {}
state_dic = {}

for item in text.split("\n"):
    if "Physical" in item:
        t = item
        name = re.findall("ge-\d\/\d\/\d", t)
        state = re.findall("En\w+", t)
        linkup = re.findall("Up", t)

for item in text.split("\n"):
    if "Des" in item:
        t = item
        description = re.findall("(?<=\bDescription:\s)(\w+\W)", t)

for item in text.split("\n"):
    if "Link-level" in item:
        t = item
        linkLevelType = re.findall("STA\w*", t)




interface = {
    "name": (' '.join(name)),
    "state": {"admin": (' '.join(state)),"link": (' '.join(linkup))},
    "description": (' '.join(description)),
    "linkLevelType": 'ethernet',
    "mtu": 1514,
    "speed": '1000000000',
    "duplex": 'full',
    "mac": '5000.0026.0000',
    "clearing": 'never',
    }


y = json.dumps(interface, indent=4)
print(y)



#t = re.findall(reg, text)