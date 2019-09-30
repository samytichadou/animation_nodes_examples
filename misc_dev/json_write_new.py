import bpy, json

# VARIABLES
debug = 0
nodetree = bpy.data.node_groups['node_creation']
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test.json"

data = {}
nodes_coll = data['nodes'] = []

# COMMON ATTRIBUTES TO GET
common_node_attributes = {'bl_idname', 'location', 'name', 'label', 'color',
                          'use_custom_color', 'useNetworkColor', 'width', 'height',
                          }
common_input_output_attributes = {'hide', 'name'
                                  }


# RETURN LIST
def returnListIfArray(object):
    if type(object) not in {str, bool, float, int}:
        try:
            iter(object)
            return list(object)
        except TypeError:
            return object
    else:
        return object


# GET NODES
def storeNodesInfos(node, dataset):
    # common attributes
    for attr in common_node_attributes:
        value = getattr(node, attr, "No value")
        dataset.update({attr: returnListIfArray(value)})
    # specific attributes
    for attr in node.__annotations__:
        value = getattr(node, attr, "No value")
        dataset.update({attr: returnListIfArray(value)})


# GET INPUTS
def storeInputOutputInfos(input, dataset):
    # common attributes
    for attr in common_input_output_attributes:
        value = getattr(input, attr, "No value")
        dataset.update({attr: returnListIfArray(value)})
    # specific attributes
    for attr in input.__annotations__:
        value = getattr(input, attr, "No value")
        dataset.update({attr: returnListIfArray(value)})


# ITERATE THROUGH NODETREE
n = 0
for node in nodetree.nodes:
    nodes_coll.append({})
    node_coll = nodes_coll[n]
    inputs_coll = node_coll['inputs'] = []
    storeNodesInfos(node, node_coll)
    # ITERATE THROUGH INPUTS
    ni = 0
    for inpt in node.inputs:
        inputs_coll.append({})
        input_coll = inputs_coll[ni]
        storeInputOutputInfos(inpt, input_coll)
        ni += 1
    n += 1
    # ITERATE THROUGH OUTPUTS

# CREATE JSON
with open(json_file, "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=False)