# listlib

import json
from time import strftime, gmtime

launch_time = strftime("%m-%d %H-%M-%S", gmtime())

pattern = [f'''<?xml version="1.0"?><plist version="1.0" gjver="2.0"><dict><k>kCEK</k><i>12</i><k>k2</k><s>''', "", '</s><k>k5</k><s>', "", '''\
</s><k>k60</k><i>13711912</i><k>k7</k><i>-1</i><k>k21</k><i>2</i><k>k47</k><t /><k>k96</k><s>''', '''</s><k>k97</k><d><k>90009001</k><d><k>kCEK</k><i>4</i><k>k1</k><i>90009001</i><k>k23</k><i>4</i><k>k2</k><s>\
Level name</s><k>k5</k><s>hexihexi</s><k>k60</k><i>13711912</i><k>k9</k><i>10</i><k>k10</k><i>50</i><k>k11</k><i>11873</i><k>k22</k><i>723</i><k>k21</k><i>3</i><k>k16</k><i>1</i><k>k45</k><i>76743</i>\
<k>k50</k><i>45</i></d><k>90009000</k><d><k>kCEK</k><i>4</i><k>k1</k><i>90009000</i><k>k23</k><i>3</i><k>k2</k><s>fetreat</s><k>k5</k><s>rewerpun</s><k>k60</k><i>23338435</i><k>k8</k><i>13</i><k>k9</k>\
<i>10</i><k>k10</k><i>50</i><k>k11</k><i>701</i><k>k22</k><i>18</i><k>k21</k><i>3</i><k>k16</k><i>1</i><k>k50</k><i>45</i><k>k48</k><i>4509</i></d></d></dict></plist>''']

def addLevel(id):
    pattern[4] += f'{id},'

def generate(levels: list = (), name="Result", author="-"):
    pattern[1] = name
    pattern[3] = author
    for level in levels:
        addLevel(level)
    return ''.join(pattern)

def advGenerate(levels: list = (), cond = "", name="Result", author="-"):
    pattern[1] = name
    pattern[3] = author
    for level in levels:
        if(eval(cond, globals(), locals())):
            addLevel(level["id"])
    return ''.join(pattern)

def save(path: str = f"D:\\Downloads\Result-{launch_time}.gmdl", content: str = ""):
    print(f"saving result as {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def readJSON(path):
    print('reading ' + path.split("\\")[-1] + '...')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(path.split("\\")[-1] + ' is successfully read')
    return data

if __name__ == "__main__":
    data = readJSON("D:\projects\py\\tkinter\Crypta\datas\\1m\data (formated).json")
    result = [level["id"] for level in data]

    print()
    print(save(content=generate(levels=result, name="ID < 1000000", author="hexihexi")))
    print(pattern[4])

