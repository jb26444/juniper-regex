import re

text = "Physical interface: ge-0/0/0, Enabled, Physical link is Up"
reg = "ge-"

t = re.findall(reg, text)
print(t)