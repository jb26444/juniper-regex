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

name = re.search("(?<=interface: )(.*)(?=\, Enabled)", t,)
state = re.search("(?<=\, )(.*)(?=\, Physical)", t)
linkup = re.search("(?<=link is )(.*)(?=)", t)
description = re.search("(?<=Description: )(.*)(?=)", t,)
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

interface = [
  {
    "name": name.group(1),
    "state": {"admin": state.group(1), "link": linkup.group(1)},
    "desr": des,
    "linkLevelType": linklevel,
    "mtu": mtu,
    "speed": sp,
    "duplex": du,
    "mac": '5000.0026.0000',
    "clearing": clear,
    "statslists": [
      {
        "type": 'traffic',
        "counters": {
          "inBytes": inbytes[0],
          "outBytes": outbytes[0],
          "inPackets": inputpackets[0],
          "outPacktes": outputpackets[0],
        },
        "load": {"inBytes": 31, "outBytes": 165, "inPkts": 0, "outPkts": 0},
      },
      {"type": 'inErrors', "counters": {"inErr": 0, "inDrops": 0}},
      {"type": 'outErrors', "counters": {"outErr": 0, "outDrops": 0}}

    ],
    "logIntList": [
      {
        "name": name.group(1),
        "protocolList": [
          {
            "protocolList": protocol[0],
            "value": {
              "value": [
                {
                  "ip": ip.group(1),
                  "mask": mask.group(1),
                  "net": net.group(1),
                  "netLong": 183586816,
                  "broadLong": 183586817,
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
            "type": 'traffic',
            "counters": {
              "inBytes": inbytes[2],
              "outBytes": outbytes[2],
              "inPkts": inputpackets[2],
              "outPkts": outputpackets[2],
            },
          },
          {
            "type": 'local',
            "counters": {
              "inBytes": inbytes[3],
              "outBytes": outbytes[2],
              "inPkts": inputpackets[2],
              "outPkts": outputpackets[2],
            },
          },
        ],
        "mtu": mtu,
      },
    ],
  },
  {
    "name": 'ae0',
    "state": {"admin": state.group(1), "link": 'up'},
    "linkLevelType": 'ethernet',
    "mtu": 1514,
    "speed": 2000000000,
    "mac": '4c96.1410.0100',
    "clearing": 'never',
    "statsList": [
      {
        "type": 'traffic',
        "counters": {
          "inBytes": 594864555,
          "outBytes": 451212986,
          "inPkts": 4483538,
          "outPkts": 4037657,
        },
        "load": {"inBytes": 425, "outBytes": 382, "inPkts": 2, "outPkts": 2},
      },
      {"type": 'inErrors', "counters": {"inErr": 0, "inDrops": 0}},
      {"type": 'outErrors', "counters": {"outErr": 0, "outDrops": 0}},
    ],
    "logIntList": [
      {
        "name": 'ae0.0',
        "dscr": 'STATIC1R18',
        "protocolList": [
          {
            "type": 'inet',
            "value": {
              "ipList": [
                {
                  "ip": '10.241.80.33',
                  "mask": 29,
                  "net": '10.241.80.32/29',
                  "netLong": 183586848,
                  "broadLong": 183586855,
                  "flagList": ['is-preferred', 'is-primary'],
                },
              ],
            },
          },
          {"type": 'iso'},
          {"type": 'mpls'},
        ],
        "statsList": [
          {
            "type": 'bundle',
            "counters": {
              "inPkts": 2247311,
              "inBytes": 317572407,
              "outPkts": 1719136,
              "outBytes": 123546352,
            },
            "load": {"inPkts": 2, "inBytes": 179, "outPkts": 0, "outBytes": 37},
          },
        ],
        "mtu": 1500,
      },
    ],
  },
]



y = json.dumps(interface, indent=4)
f = open("results.json", "a")
f.write(y)
f.close()
print(y)

fh.close()
os.remove("file1.txt")
os.remove("file2.txt")

