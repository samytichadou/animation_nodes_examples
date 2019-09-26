import bpy
import json

json_file = r"/home/tonton/Bureau/test2.json"

data = {}
nodetree_coll = data['nodetree'] = {}
for i in range(0,10):
    nodetree_coll.update({str(i) : i})
    
nodes_coll = data['nodes'] = []
node1 = nodes_coll.append({'node1':1})
node1.update({'inputs' : []})

with open(json_file, "w") as write_file :
    json.dump(data, write_file, indent=4, sort_keys=False)