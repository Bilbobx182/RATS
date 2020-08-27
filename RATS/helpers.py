# Make this less generic when more specific helpers are needed. For now it's OK.
import json


def get_json(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f"Whoops! An error occured {ex}")
