import re
import json


# En\w+ - Enable whole word
# ge-\d\/\d\/\d - ge

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
        t = (item.strip())
        name = re.findall(reg, t)
        state = re.findall(reg1, t)
        link = re.findall(reg2, t)


int_dic.update({'Name': name})
state_dic.update({'State': state})
state_dic.update({'link': link})
int_dic.update(state_dic)
print(int_dic)

#t = re.findall(reg, text)