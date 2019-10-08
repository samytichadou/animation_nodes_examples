import bpy
import json


# get properties
def get_properties(obj):
    is_point_coll = False
    collections = []
    pointers = []
    floats_ints_bools = []
    for prop in obj.bl_rna.properties:
        if prop.type not in {'POINTER', 'COLLECTION'}:
            floats_ints_bools.append(prop)
        elif prop.type == 'POINTER':
            is_point_coll = True
            pointers.append(prop)
        elif prop.type == 'COLLECTION':
            is_point_coll = True
            collections.append(prop)
    return floats_ints_bools, collections, pointers, obj, is_point_coll


# store float int bools in dataset
def store_float_int_bools(obj, prop_list, dataset):
    for prop in prop_list:

        value = getattr(obj, prop.identifier, "No value")

        if prop.type == 'FLOAT':
            try:
                lgt = len(value)
                list = []
                for i in range(0, lgt):
                    list.append(value[i])
                    # dataset[prop.identifier].append(value[i])
                dataset.update({prop.identifier: list})
            except TypeError:
                # dataset[prop.identifier].append(value)
                dataset.update({prop.identifier: value})
        else:
            # dataset[prop.identifier].append(value)
            dataset.update({prop.identifier: value})


# create dataset from pointer
def create_dataset_from_pointer(obj, pointer_list, dataset):
    sub_dataset_list = []
    for pointer in pointer_list:
        value = getattr(obj, pointer.identifier, "No value")
        new = dataset[value.bl_rna.properties.identifier] = {}
        sub_dataset_list.append(new)
    return sub_dataset_list


# DOING
print()
print()

# VARIABLES
nodetree = bpy.data.node_groups['NodeTree']
# nodetree=bpy.data.materials['test'].node_tree

# json_file = r"C:\Users\crossrivergraph8\Desktop\test.json"
# json_file = r"/home/tonton/Bureau/test.json"
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test.json"

# JSON
data = {}
nodetree_coll = data['nodetree'] = {}
nodes_coll = data['nodes'] = []
links_coll = data['links'] = []

# GET NODETREE INFOS
prop, coll, pointers, object, is_point_coll = get_properties(nodetree)
store_float_int_bools(nodetree, prop, nodetree_coll)

# GET NODES INFOS
i = -1
for node in nodetree.nodes:
    i += 1
    nodes_coll.append({})
    prop, coll, pointers, object2, is_point_coll = get_properties(node)
    store_float_int_bools(node, prop, nodes_coll[i])

    # GET INPUTS
    inputs_coll = nodes_coll[i]['inputs'] = []
    i2 = -1
    for input in node.inputs:
        i2 += 1
        inputs_coll.append({})
        prop, coll, pointers, object2, is_point_coll = get_properties(input)
        store_float_int_bools(input, prop, inputs_coll[i2])

    # GET OUTPUTS
    outputs_coll = nodes_coll[i]['outputs'] = []
    i3 = -1
    for output in node.outputs:
        i3 += 1
        outputs_coll.append({})
        prop, coll, pointers, object2, is_point_coll = get_properties(output)
        store_float_int_bools(output, prop, outputs_coll[i3])

i = -1
# GET LINKS
for link in nodetree.links:
    i += 1
    links_coll.append({})
    prop, coll, pointers, object2, is_point_coll = get_properties(link)
    store_float_int_bools(link, prop, links_coll[i])

    # GET FROM NODE NAME
    for pointer in pointers:
        if pointer.identifier != 'bl_rna':
            value = getattr(link, pointer.identifier, "No value")
            links_coll[i].update({pointer.identifier: value.name})

with open(json_file, "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=False)
