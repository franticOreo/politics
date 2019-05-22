# This script will input a sentance
# this sentance will be then linked to a politicians name
# and their respective party


import json


input = "Mr Andrew Wallace MP"

with open('politicians_and_parties.json', 'r') as json_file:
    data = json.load(json_file)
    # print(type(data))
    for dict in data:
        for key, val in dict.items():
            # if the name key matches the input string, return the party value
            # print('{} = {}'.format(key, val))
            if val == input:
            #     print(True)
            # if input in key:
                print(dict['party'])
