import bpy
import json

ntree=bpy.data.node_groups['NodeTree.001']

#ntree.nodes.new("an_MeshObjectInputNode")

#json_file = r"/home/tonton/Bureau/test.json"
json_file = r"C:\Users\crossrivergraph8\Desktop\test.json"

#READ FUNCTION
def read_json(filepath):
    with open(filepath, "r") as read_file:
        datas = json.load(read_file)
    return datas

#DOING
print()
print()
datas=read_json(json_file)
#print(datas['nodes'])

#NODETREE
for attr in datas['nodetree']:
    try:
        setattr(ntree, attr, datas['nodetree'][attr])
    except:
        print('error')
        pass

#NODES
for n in datas['nodes']:
    #create
    node=ntree.nodes.new(n['bl_idname'])
    #set attribute
    for attr in n:
        if attr != 'identifier':
            try:
                setattr(node, attr, n[attr])
            except:
                print('error')
                pass
        
