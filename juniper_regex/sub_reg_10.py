import json
import re
import os

text = open('file2.txt', 'r')
t = text.read()

name = re.search("(?<=interface: )(.*)(?=\, Enabled)", t,)
state = re.search("(?<=\, )(.*)(?=\, Physical)", t)
linkup = re.search("(?<=link is )(.*)(?=)", t)
description = re.search("(?<=Description: )(.*)(?=)", t,)
des = description.group(1)
linkLevelType = re.search("(?<=type: )(.*)(?=\, MTU)", t)
linklevel = linkLevelType.group(1)
mtu_search = re.search("(?<=MTU: )(\d*)(?=\,)", t)
mtu = mtu_search.group(1)
speed = re.search("(?<=Speed: )(.*)(?=\d*\, B)", t)
sp = speed.group(1)
clearing = re.search("(?<=cleared: )(.*)(?=)", t)
clear = clearing.group(1)
inbytes = re.findall("Input\s*bytes\s*\:\s*(\d*)", t)
outbytes = re.findall("Output\s*bytes\s*\:\s*(\d*)", t)
inputpackets = re.findall("Input\s*packets\s*\:\s*(\d*)", t)
outputpackets = re.findall("Output\s*packets\s*\:\s*(\d*)", t)
protocol = re.findall("Protocol (.*)(?=\,\sMTU)", t)
ip = re.search("Local: (.*)(?=\, B)", t)
mask = re.search("\/(.*)(?=\,\sLocal)", t)
net = re.search("Destination: (.*)(?=\,\sLocal)", t)
flag = re.search("Addresses, Flags: (.*)(?=\s\w)\s(.*)(?=)", t)
mac = re.findall("(?<=Hardware\saddress: )(.*)(?=)", t)
macaddress = ''.join([str(elem) for elem in mac])
macformat = str(macaddress).replace(':', '')
macdd = macformat[:4] + "." + macformat[4:8]+ "." + macformat[8:]
inouterrors =  re.findall("Errors:\s(\d*)", t)
dropps = re.findall("Drops:\s(\d*)", t)
bundleinp = re.findall("Bundle:\s*Input\s\:\s*(\d*)", t)
bundleinb = re.search("Bundle:\s*Input\s\:\s*(\d*)\s*(\d*)\s*(\d*)", t)
bundleout = re.search("Bundle:\s(.*)\s*Output:\s*(\d*)\s*(\d*)\s*(\d*)", t)

interface = [
  {
    "name": name.group(1),
    "state": {"admin": state.group(1), "link": linkup.group(1)},
    "linkLevelType": linklevel,
    "mtu": mtu,
    "speed": sp,
    "mac": macdd,
    "clearing": clear,
    "statsList": [
      {
        "type": "traffic",
        "counters": {
          "inBytes": inbytes[0],
          "outBytes": outbytes[0],
          "inPkts": inputpackets[0],
          "outPkts": outputpackets[0],
        },
        "load": {"inBytes": 425, "outBytes": 382, "inPkts": 2, "outPkts": 2},
      },
      {"type": "inErrors", "counters": {"inErr": inouterrors[0], "inDrops": dropps[0]}},
      {"type": "outErrors", "counters": {"outErr": inouterrors[1], "outDrops": dropps[1]}},
    ],
    "logIntList": [
      {
        "name": name.group(1),
        "dscr": des,
        "protocolList": [
          {
            "type": protocol[0],
            "value": {
              "ipList": [
                {
                  "ip": ip.group(1),
                  "mask": mask.group(1),
                  "net": net.group(1),
                  "netLong": 183586848,
                  "broadLong": 183586855,
                  "flagList": [flag.group(1), flag.group(2)],
                },
              ],
            },
          },
          {"type": protocol[1]},
          {"type": protocol[2]},
        ],
        "statsList": [
          {
            "type": 'bundle',
            "counters": {
              "inPkts": bundleinp,
              "inBytes": bundleinb.group(3),
              "outPkts": bundleout.group(2),
              "outBytes": bundleout.group(4),
            },
            "load": {"inPkts": 2, "inBytes": 179, "outPkts": 0, "outBytes": 37},
          },
        ],
        "mtu": mtu,
      },
    ],
  },
]


y = json.dumps(interface, indent=4)
f = open("results.json", "a")
z = y.replace('"', '')
f.write("\n" + z[1:])
f.close()
print(z)