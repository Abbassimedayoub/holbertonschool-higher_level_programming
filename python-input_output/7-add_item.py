#!/usr/bin/python3
from sys import *

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
try:
    list = load(filename)
except Exception:
    list = []
for arg in argv[1:]:
    list.append(arg)
save(list, filename)
