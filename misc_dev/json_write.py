import bpy
import json

#node = bpy.data.materials['Material'].node_tree.nodes["Principled BSDF"]
#node = bpy.data.node_groups['NodeTree'].nodes['Offset Matrix']
#nodetree = bpy.data.node_groups['NodeTree']
nodetree=bpy.data.materials['Material'].node_tree

json_file = r"/home/tonton/Bureau/test.json"

#JSON
data = {}
nodetree_coll = data['nodetree'] = {}
nodes_coll = data['nodes'] = {}
#FUNCTION
def iterate(obj, dataset):
    for prop in obj.bl_rna.properties:
        if prop.type not in {'POINTER','COLLECTION'}:
            value=getattr(obj, prop.identifier, "No value")
            #dataset[prop.identifier]=[]
            if prop.type=='FLOAT':
                try :
                    lgt=len(value)
                    list=[]
                    for i in range (0, lgt):
                        list.append(value[i])
                        #dataset[prop.identifier].append(value[i])
                    dataset.update({prop.identifier : list})
                except TypeError:
                    #dataset[prop.identifier].append(value)
                    dataset.update({prop.identifier : value})
            else:
                #dataset[prop.identifier].append(value)
                dataset.update({prop.identifier : value})


#DOING
iterate(nodetree, nodetree_coll)
for node in nodetree.nodes :
    nd = nodes_coll[node.name] = {}
    iterate(node, nd)
    inputs_coll = nd["inputs"] = {}
    outputs_coll = nd["outputs"] = {} 
               
    iterate(node, nd)

    for ipt in node.inputs:
        input = inputs_coll[ipt.name] = {}
        iterate(ipt, input)
        
    for opt in node.outputs:
        output = outputs_coll[opt.name] = {}
        iterate(opt, output)
    
    
with open(json_file, "w") as write_file :
    json.dump(data, write_file, indent=4, sort_keys=False)