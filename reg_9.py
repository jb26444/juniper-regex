import json
import re
import os

with open('source.txt', 'r') as fh:
    text_split = fh.read().split("Physical interface:")

with open('file1.txt', 'w') as fh:
    fh.write("Physical interface:" + text_split[1])

with open('file2.txt', 'w') as fh:
    fh.write("Physical interface:" + text_split[2])

text = open('file1.txt', 'r')
t = text.read()

text = open('file2.txt', 'r')
k = text.read()

name = re.search("(?<=interface: )(.*)(?=\, Enabled)", t, )
state = re.search("(?<=\, )(.*)(?=\, Physical)", t)
linkup = re.search("(?<=link is )(.*)(?=)", t)
description = re.search("(?<=Description: )(.*)(?=)", t, )
des = description.group(1)
linkLevelType = re.search("(?<=type: )(.*)(?=\, MTU)", t)
linklevel = linkLevelType.group(1)
mtu_search = re.search("(?<=MTU: )(.*)(?=\d*\, Link)", t)
mtu = mtu_search.group(1)
speed = re.search("(?<=Speed: )(.*)(?=\d*\, B)", t)
sp = speed.group(1)
duplex = re.search("(?<=Link-mode: )(.*)(?=\-duplex)", t)
du = duplex.group(1)
clearing = re.search("(?<=cleared: )(.*)(?=)", t)
clear = clearing.group(1)
inbytes = re.findall("Input\s*bytes\s*\:\s*(\d*)", t)
outbytes = re.findall("Output\s*bytes\s*\:\s*(\d*)", t)
inputpackets = re.findall("Input\s*packets\s*\:\s*(\d*)", t)
outputpackets = re.findall("Output\s*packets\s*\:\s*(\d*)", t)
protocol = re.findall("Protocol (.*)(?=\,\sMTU)", t)
ip = re.search("Local: (.*)(?=\, B)", t)
mask = re.search("\/(.*)(?=\sLocal)", t)
net = re.search("Destination: (.*)(?=\,\sLocal)", t)
flag = re.search("Addresses, Flags: (.*)(?=\s\w)\s(.*)(?=)", t)



y = json.dumps(interface, indent=4)
f = open("results.json", "a")
f.write(y)
f.close()
print(y)

fh.close()
os.remove("file1.txt")
os.remove("file2.txt")
