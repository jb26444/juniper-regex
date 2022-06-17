import json
import re
import os

if os.path.exists("results.json"):
  os.remove("results.json")
else:
  pass


with open('source.txt', 'r') as fh:
  text_split = fh.read().split("Physical interface:")

with open('file1.txt', 'w') as fh:
  fh.write("Physical interface:" + text_split[1])

with open('file2.txt', 'w') as fh:
  fh.write("Physical interface:" + text_split[2])

text = open('file1.txt', 'r')
t = text.read()


name = re.search("(?<=interface: )(.*)(?=\, Enabled)", t,)
state = re.search("(?<=\, )(.*)(?=\, Physical)", t)
linkup = re.search("(?<=link is )(.*)(?=)", t)
description = re.search("(?<=Description: )(.*)(?=)", t,)
des = description.group(1)
linkLevelType = re.search("(?<=type: )(.*)(?=\, MTU)", t)
linklevel = linkLevelType.group(1)
mtu_search = re.findall("(?<=MTU: )(\d*)(?=\,)", t)
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
mask = re.search("\/(.*)(?=\,\sLocal)", t)
net = re.search("Destination: (.*)(?=\,\sLocal)", t)
flag = re.search("Addresses, Flags: (.*)(?=\s\w)\s(.*)(?=)", t)
mac = re.findall("(?<=Hardware\saddress: )(.*)(?=)", t)
macaddress = ''.join([str(elem) for elem in mac])
macformat = str(macaddress).replace(':', '')
macdd = macformat[:4] + "." + macformat[4:8]+ "." + macformat[8:]
inouterrors =  re.findall("Errors:\s(\d*)", t)
dropps = re.findall("Drops:\s(\d*)", t)


interface = [
  {
    "name": name.group(1),
    "state": {"admin": state.group(1), "link": linkup.group(1)},
    "desr": des,
    "linkLevelType": linklevel,
    "mtu": mtu_search[0],
    "speed": sp,
    "duplex": du,
    "mac": macdd,
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
      {"type": 'inErrors', "counters": {"inErr": inouterrors[0], "inDrops": dropps[0]}},
      {"type": 'outErrors', "counters": {"outErr": inouterrors[1], "outDrops": dropps[1]}}

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
        "mtu": mtu_search[1],
      },
    ],
  },
]


y = json.dumps(interface, indent=4)
f = open("results.json", "a")
z = y.replace('"', '')
f.write(z[:-1])
f.close()
print(z)

os.system("python sub_reg_10.py")

fh.close()
os.remove("file1.txt")
os.remove("file2.txt")

