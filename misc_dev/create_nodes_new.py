import bpy, json

# VARIABLES
debug=0
nodetree = bpy.data.node_groups['node_creation']
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test.json"

# READ FUNCTION
def read_json(filepath):
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
    return data

# SET ATTRIBUTES
def setAttributesFromDict(object, dataset):
    for attr in dataset:
        try:
            setattr(object, attr, dataset[attr])
        except AttributeError as err:
            if debug: print(err)

# CREATE NODES
data=read_json(json_file)
for node in data['nodes']:
    newnode=nodetree.nodes.new(node['bl_idname'])
    #node attributes
    setAttributesFromDict(newnode, node)

    #inputs
    #create missing
    diff=len(node['inputs'])-len(newnode.inputs)
    for i in range(0, diff):
        newnode.newInputSocket()
    ni=0
    for inpt in node['inputs']:
        input=newnode.inputs[ni]
        setAttributesFromDict(input, inpt)
        ni+=1