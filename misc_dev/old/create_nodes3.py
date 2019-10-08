import bpy
import json


#ntree=bpy.data.node_groups['NodeTree']
#ntree = bpy.data.materials['test'].node_tree
ntree=bpy.data.node_groups.new('imported', 'an_AnimationNodeTree')

# ntree.nodes.new("an_MeshObjectInputNode")

# json_file = r"/home/tonton/Bureau/test.json"
json_file = r"/home/tonton/Taf/code/animation_nodes_examples/misc_dev/test2.json"


# READ FUNCTION
def read_json(filepath):
    with open(filepath, "r") as read_file:
        datas = json.load(read_file)
    return datas


# SET ATTRIBUTE
def set_attribute(obj, dataset, avoid_identifier):
    for attr in dataset:
        if attr != 'identifier' or not avoid_identifier:
            # print(dataset[attr])
            try:
                setattr(obj, attr, dataset[attr])
                print('---set : ' + attr)
            except:
                print('---error : ' + attr)
                pass


# DOING
print()
print()
datas = read_json(json_file)

# NODETREE
#set_attribute(ntree, datas['nodetree'], True)

# NODES
for node in datas['nodes']:
    # create
    newnode = ntree.nodes.new(node['bl_idname'])
    # set attribute
    set_attribute(newnode, node, True)

    # INPUTS
    print()
    print()
    print()
    print()
    print()
    i=-1
    for input in node['inputs']:
        i+=1
        try:
            inp=newnode.inputs[i]
            setattr(inp, 'default_value', input['default_value'])
            print('set')
        except:
            print('nop')
            pass

# LINKS
for link in datas['links']:
    # create
    inp = ntree.nodes[link['from_node']].outputs[link['from_socket']]
    outp = ntree.nodes[link['to_node']].inputs[link['to_socket']]
    newlink = ntree.links.new(inp, outp)
    # set attribute
    set_attribute(newlink, link, True)
