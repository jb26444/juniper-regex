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
inbytes = re.search("Input\s*bytes\s*\:\s*(\d*)", t)
inbytesgroup = inbytes.group(1)
outbytes = re.search("Output\s*bytes\s*\:\s*(\d*)", t)
outbytesgroup = outbytes.group(1)
inputpackets = re.search("Input\s*packets\s*\:\s*(\d*)", t)
inputpacketsgroup = inputpackets.group(1)
outputpackets = re.search("Output\s*packets\s*\:\s*(\d*)", t)
outputpacketsgroup = outputpackets.group(1)
protocol = re.findall("Protocol (.*)(?=\,\sM)", t, flags=re.MULTILINE)


#interface = dict(name=str(name), state={ "admin": state, "link": (' '.join(linkup))}, description=des,
                 #linkLevelType=linklevel, mtu=mtu, speed=sp + str("000"), duplex=du, mac='5000.0026.0000',
                # clearing=clear, statistic={"statistic:": state, "link": linkup })


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
          "inBytes": inbytesgroup,
          "outBytes": outbytesgroup,
          "inPackets": inputpacketsgroup,
          "outPacktes": outputpacketsgroup,
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
            "protocolList": protocol,
            "value": {
              "value": [
                {
                  "ip": '10.241.80.1',
                  "mask": 31,
                  "net": '10.241.80.0/31',
                  "netLong": 183586816,
                  "broadLong": 183586817,
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
            "type": 'traffic',
            "counters": {
              "inBytes": 79748727,
              "outBytes": 160678589,
              "inPkts": 1115935,
              "outPkts": 1591473,
            },
          },
          {
            "type": 'local',
            "counters": {
              "inBytes": 69656698,
              "outBytes": 150343645,
              "inPkts": 951675,
              "outPkts": 1424433,
            },
          },
        ],
        "mtu": 1500,
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
print(y)

# t = re.findall(reg, text)
