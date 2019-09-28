import bpy
import json

# node = bpy.data.materials['Material'].node_tree.nodes["Principled BSDF"]
# node = bpy.data.node_groups['NodeTree'].nodes['Offset Matrix']
# nodetree = bpy.data.node_groups['NodeTree']
nodetree = bpy.data.materials['Material'].node_tree

# json_file = r"C:\Users\crossrivergraph8\Desktop\test.json"
json_file = r"/home/tonton/Bureau/test.json"

# JSON
data = {}
nodetree_coll = data['nodetree'] = {}


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


#
def recursive_data_storing(obj, data):
    prop, coll, pointers, object, is_point_coll = get_properties(obj)
    store_float_int_bools(nodetree, prop, nodetree_coll)


# DOING
print()
print()
prop, coll, pointers, object, is_point_coll = get_properties(nodetree)
store_float_int_bools(nodetree, prop, nodetree_coll)

print(object)
for c in coll:
    print()
    print(c.identifier)
    data[c.identifier] = []
    i = -1
    for obj in eval("object.%s" % c.identifier):
        i += 1
        data[c.identifier].append({})
        prop, coll, pointers, object2, is_point_coll = get_properties(obj)
        store_float_int_bools(obj, prop, data[c.identifier][i])
        print(coll)
        print()
        print(pointers)

with open(json_file, "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=False)
