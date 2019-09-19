URL=r"https://raw.githubusercontent.com/samytichadou/animation_nodes_examples/master/README.md"


##########################
#check internet connection
##########################
from socket import create_connection

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        create_connection(("www.duckduckgo.com", 80))
        return True
    except OSError:
        pass
    return False


##########################
#get file from address
##########################
from urllib import request

tmp=r"C:\Users\crossrivergraph8\Desktop\readme_test.md"

request.urlretrieve(URL, tmp)


##########################
#open website
##########################
import bpy

bpy.ops.wm.url_open(url=URL)


##########################
#delete temp with error handling
##########################
from os import remove

try: 
    os.remove(tmp) 
    print("% s removed successfully" % path) 
except OSError as error: 
    print(error) 
    print("File path can not be removed") 


##########################
#json content
##########################
- blender version
- category

- examples
    - b version
    - category
    - nodetree
    - nodetree preview
    - nodetree result
    - youtube link
    - howto.txt
    - tags.txt
