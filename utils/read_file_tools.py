import os
import json


def read_file_to_list(file_path: str):
    if not os.path.exists(file_path):
        return None
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r') as file:
        return file.readlines()


def read_file_to_str(file_path: str, connector=""):
    if not os.path.exists(file_path):
        return None
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r') as file:
        return connector.join(file.readlines())


def read_json_file(file_path: str):
    if not os.path.exists(file_path):
        return None
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r') as file:
        return json.load(file)


def read_json_to_object(file_path: str, decoder:json.JSONDecoder):
    if not os.path.exists(file_path):
        return None
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r') as file:
        return json.load(file, cls=decoder)


def write_to_file(file_path: str, content: str):
    with open(file_path, 'w') as file:
        file.write(content)


def split_proj_ids_file(file_path):
    """
    param file_path: str for txt file which saves content like "proj1:id1,id2,id3\nproj2:id"
    return: a list of tuple like [(proj, id)]
    """
    lines = read_file_to_list(file_path)
    proj_id_lst = []
    for proj_ids in lines:
        proj = proj_ids[:proj_ids.find(':')]
        ids = proj_ids[proj_ids.find(':') + 1:].split(',')
        for id in ids:
            proj_id_lst.append((proj, id.strip()))
    return proj_id_lst
