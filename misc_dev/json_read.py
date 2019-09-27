import bpy
import json

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

for n in datas['nodes']:
    print()
    print()
    print(n['name'])
    print()
    print('INPUTS')
    for i in n['inputs']:
        print(i['name'])
    print()
    print('OUTPUTS')
    for o in n['outputs']:
        print(o['name'])
