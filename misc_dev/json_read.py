import bpy
import json

json_file = r"/home/tonton/Bureau/test.json"

#READ FUNCTION
def read_json(filepath):
    with open(filepath, "r") as read_file:
        datas = json.load(read_file)
    return datas

#DOING
print()
print()
datas=read_json(json_file)
print(datas['nodes']['Material Output'])
print(datas['nodes']['Material Output']['bl_label'])

for n in datas['nodes']:
    print(n)