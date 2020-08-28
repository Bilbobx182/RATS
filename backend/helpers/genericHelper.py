# Make this less generic when more specific helpers are needed. For now it's OK.
import json
from datetime import datetime


class GenericHelper:

    def remove_duplicates_in_dict(self, input_dictionary):
        return_data = []
        for item in input_dictionary:
            if item not in return_data:
                return_data.append(item)
        return return_data

    def get_datetime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def get_json(self, filename):
        try:
            with open(filename) as json_file:
                return json.load(json_file)
        except Exception as ex:
            print(f"Whoops! An error occured {ex}")
