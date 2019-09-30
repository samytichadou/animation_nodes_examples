import bpy
import json

debug = True

# ntree=bpy.data.node_groups['NodeTree']
# ntree = bpy.data.materials['test'].node_tree
ntree = bpy.data.node_groups.new('imported', 'an_AnimationNodeTree')
# ntree=bpy.data.node_groups['node_creation']

# ntree.nodes.new("an_MeshObjectInputNode")

# json_file = r"/home/tonton/Bureau/test.json"
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test2.json"


# READ FUNCTION
def read_json(filepath):
    with open(filepath, "r") as read_file:
        datas = json.load(read_file)
    if debug: print("---Reading " + filepath)
    return datas


# SET ATTRIBUTE
def set_attribute(obj, dataset, avoid_identifier):
    if debug: print('---Setting attribute')
    for attr in dataset:
        if attr != 'useMatrixList':
            if attr != 'identifier' or not avoid_identifier:
                # print(dataset[attr])
                try:
                    setattr(obj, attr, dataset[attr])
                    if debug: print(' ---set : ' + attr)
                except:
                    if debug: print(' ---error : ' + attr)
                    pass


# DOING
print()
print()
datas = read_json(json_file)

# NODETREE
# set_attribute(ntree, datas['nodetree'], True)

if debug:
    print('---NODES---')
    print()

# NODES
for node in datas['nodes']:
    if debug: print('---creating Node ' + node['name'])
    # create
    newnode = ntree.nodes.new(node['bl_idname'])
    # set attribute
    set_attribute(newnode, node, True)

    # INPUTS
    if debug:
        print()
        print('---INPUTS---')
        print()
    i = -1
    for input in node['inputs']:
        if debug: print('---setting  input ' + input['name'])
        i += 1
        try:
            inp = newnode.inputs[i]
            setattr(inp, 'default_value', input['default_value'])
            if debug: print(' ---set : default_value')
        except:
            if debug: print(' ---error : default_value')
            pass

if debug:
    print('---LINKS---')
    print()
# LINKS
for link in datas['links']:
    if debug: print('---setting  link between ' + link['from_node'] + ' and ' + link['to_node'])
    # create
    inp = ntree.nodes[link['from_node']].outputs[link['from_socket_index']]
    outp = ntree.nodes[link['to_node']].inputs[link['to_socket_index']]
    print(link['from_node'])
    print(link['to_node'])
    ntree.links.new(inp, outp)
    # set attribute
    # set_attribute(newlink, link, True)
