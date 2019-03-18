import sys
import json

input_filename = sys.argv[1]
output_filename = sys.argv[2]


def retrieve_json(filename):
    with open(filename, 'r') as infile:
        unformated_json = json.load(infile)
    return unformated_json


def write_json(filename, unformated_json):
    new_json = json.dumps(unformated_json)
    with open(filename, 'w') as outfile:
        outfile.write(new_json)


def split_parent(parent):
    return parent.split("folder")


def get_depth(myjson):
    depth = 0
    for node in myjson:
        parent_number = split_parent(node["parent"])
        if parent_number[0] != "root" and depth < int(parent_number[1]):
            depth = int(parent_number[1])
    return depth


def find_root(myjson):
    for node in myjson:
        if node["parent"] == "root":
            return node


def find_children(depth_level, myjson):
    children = []
    for node in myjson:
        parent_number = split_parent(node["parent"])
        if parent_number[0] != "root" and int(parent_number[1]) == depth_level:
            if node['type'] == "folder":
                node['children'] = find_children(depth_level+1, myjson)
            children.append(node)
    return children


myjson = retrieve_json(input_filename)
depth = get_depth(myjson)
new_json = [find_root(myjson)]
new_json[0]['children'] = find_children(1, myjson)
write_json(output_filename, new_json)
