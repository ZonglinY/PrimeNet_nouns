import json

a = json.load(open("Data/graph_may_30_2205.json"), encoding='utf-8')

# load ordered list json
ordered_list = json.load(open("ordered_list.json"), encoding='utf-8')

pnet = open('primenet_ordered.py','w')
pnet.write("primenet = {}\n")
for key in ordered_list:
    pnet.write("primenet['"+key+"'] = [")
    for i in range(len(a[key])):
        pnet.write("'" + a[key][i] + "'")
        if i < len(a[key])-1: pnet.write(", ")
        else: pnet.write("")
    pnet.write("]\n")

