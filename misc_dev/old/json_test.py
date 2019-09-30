import bpy
import json

json_file = r"C:\Users\crossrivergraph8\Desktop\test2.json"

data = {}
nodetree_coll = data['nodetree'] = {}
for i in range(0,10):
    nodetree_coll.update({str(i) : i})
    
nodes_coll = data['nodes'] = []
data['nodes'].append({})
data['nodes'][0].update({'inputs' : []})

with open(json_file, "w") as write_file :
    json.dump(data, write_file, indent=4, sort_keys=False)
