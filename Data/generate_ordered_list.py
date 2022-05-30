import json

# load graph_may_30_2205.json
with open('graph_may_30_2205.json') as json_file:
    G_dict = json.load(json_file)

ordered_list = []

def put_to_ordered_list(dictionary, ordered_list):
    for key in dictionary:
        ordered_list.append(key)
        put_to_ordered_list(dictionary[key], ordered_list)

put_to_ordered_list(G_dict, ordered_list)

# save ordered_list.json
with open('ordered_list.json', 'w') as outfile:
    json.dump(ordered_list, outfile)