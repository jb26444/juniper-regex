import json
import re

# En\w+ - Enable whole word
# ge-\d\/\d\/\d - ge
# int_dic.update({'Name': name})
# state_dic.update({'State': state})
# state_dic.update({'link': link})
# int_dic.update(state_dic)
# (' '.join(fruits)) - remove square brackets

#text = """const text = `


text = open('source.txt', 'r')
t = text.read()

#m = re.search('name\s\w+\s(\w+)',s)
#interface:\sge-\d\/\d\/\d\,\s(\w*)

name = re.findall("ge-\d\/\d\/\d", t,)[0]
state = re.findall("En\w+", t)
linkup = re.findall("Up", t)
description = re.search("Description:\s(\w*)", t,)
des = description.group(1)
linkLevelType = re.search("Link-level\ type:\s(\w*)", t)
linklevel = linkLevelType.group(1)
mtu_search = re.search("MTU:\s(\w*)", t)
mtu = mtu_search.group(1)
speed = re.search("Speed:\s(\d*)", t)
sp = speed.group(1)
duplex = re.search("(Full)\-(\w*)", t)
du = duplex.group(1)
clearing = re.search("cleared:\s(\w*)", t)
clear = clearing.group(1)


interface = dict(name=str(name), state={"admin": (' '.join(state)), "link": (' '.join(linkup))}, description=des,
                 linkLevelType=linklevel, mtu=mtu, speed=sp + str("000"), duplex=du, mac='5000.0026.0000',
                 clearing=clear,)


y = json.dumps(interface, indent=4)
print(y)

# t = re.findall(reg, text)
