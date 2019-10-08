import bpy, json

# VARIABLES
debug = 1
nodetree = bpy.data.node_groups['node_creation']
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test.json"

data = {}
nodes_coll = data['nodes'] = []

# COMMON ATTRIBUTES TO GET
common_node_attributes = {'bl_idname', 'location', 'name', 'label', 'color',
                          'use_custom_color', 'useNetworkColor', 'width', 'height',
                          }
common_input_attributes = {'hide', 'name'
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


# CHECK SERIALIZABLE
def isSerializable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False


# STORE INFOS
def storeObjectInfos(object, dataset, objecttype):
    if debug: print(objecttype + " - " + object.name)
    if objecttype == 'nodes':
        common = common_node_attributes
    elif objecttype == 'inputs':
        common = common_input_attributes
    # common attributes
    try:
        for attr in common:
            # for attr in object.bl_rna.properties:
            value = returnListIfArray(getattr(object, attr, "No value"))
            if isSerializable(value):
                dataset.update({attr: value})
                if debug: print("--- adding to dataset - " + attr + " - " + str(value))
            else:
                if debug: print("xxx not serializable - " + attr + " - " + str(value))
    except AttributeError as err:
        if debug:
            print("xxx error when adding to dataset - " + attr)
            print("xxx " + str(err))
    # specific attributes
    try:
        for attr in object.__annotations__:
            value = getattr(object, attr, "No value")
            if isSerializable(returnListIfArray(value)):
                dataset.update({attr: returnListIfArray(value)})
                if debug: print("--- adding to dataset - " + attr)
            else:
                if debug: print("xxx not serializable - " + attr)
    except AttributeError as err:
        if debug:
            print("xxx error when adding to dataset - " + attr)
            print("xxx " + str(err))


# STORE PARENT
def storeNodeParentObject(node, dataset):
    # get node's parent object
    if node.parent is not None:
        dataset.update({'parent': node.parent.name})


# ITERATE THROUGH NODETREE
n = 0
for node in nodetree.nodes:
    nodes_coll.append({})
    node_coll = nodes_coll[n]
    inputs_coll = node_coll['inputs'] = []
    storeObjectInfos(node, node_coll, 'nodes')
    storeNodeParentObject(node, node_coll)
    # ITERATE THROUGH INPUTS
    ni = 0
    for inpt in node.inputs:
        inputs_coll.append({})
        input_coll = inputs_coll[ni]
        storeObjectInfos(inpt, input_coll, 'inputs')
        ni += 1
    n += 1

# CREATE JSON
with open(json_file, "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=False)