import bpy
import json

#node = bpy.data.materials['Material'].node_tree.nodes["Principled BSDF"]
#node = bpy.data.node_groups['NodeTree'].nodes['Offset Matrix']
#nodetree = bpy.data.node_groups['NodeTree']
nodetree=bpy.data.materials['Material'].node_tree

json_file = r"C:\Users\crossrivergraph8\Desktop\test.json"
#json_file = r"/home/tonton/Bureau/test.json"

#JSON
data = {}
nodetree_coll = data['nodetree'] = {}
nodes_coll = data['nodes'] = []
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
i = -1
for node in nodetree.nodes :
    i += 1
    nodes_coll.append({})
    iterate(node, nodes_coll[i])
    
    #inputs_coll = nd["inputs"] = {}
    #outputs_coll = nd["outputs"] = {} 
    data['nodes'][i].update({'inputs' : []})
    data['nodes'][i].update({'outputs' : []})
    
    i1 = -1
    i2 = -1
    
    for ipt in node.inputs:
        i1 += 1
        data['nodes'][i]['inputs'].append({})
        input = data['nodes'][i]['inputs'][i1]
        iterate(ipt, input)
        
    for opt in node.outputs:
        i2 += 1
        data['nodes'][i]['outputs'].append({})     
        output = data['nodes'][i]['outputs'][i2]   
        iterate(opt, output)
    
    
with open(json_file, "w") as write_file :
    json.dump(data, write_file, indent=4, sort_keys=False)
