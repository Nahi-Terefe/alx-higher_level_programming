#!/usr/bin/python3
"""module for task 9 script"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
my_list = []
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
my_list = my_list + sys.argv[1:]
save_to_json_file(my_list, "add_item.json")