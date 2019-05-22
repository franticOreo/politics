'''
This script will capture statements by politicans
It will save their statement and name
the output of the name will be for the 'find_party.py' script
'''

import re
import json



pattern = re.compile('(:?(Senator|Mr|Ms|Dr)\s+([A-Z]{2,})\s*(\(.+?\))\s+(\(\d{2}:\d{2}\):)(.*?))(?=(Senator|Mr|Ms|Dr)\s+([A-Z]{2,}))')


# CLEANING FILE
# open file and remove \n space
with open('speech/speach.txt', 'r') as dirty_speech:
    text = dirty_speech.read()
    text = text.replace(r'\n', '')
    text = text.replace(r'\t', '')
    text = text.replace(r'\\', '')
    with open('speech_cleaned.txt', "w") as clean_speech:
        clean_speech.write(text)

clean_speech_text = open('speech_cleaned.txt').read()

list_name_speech = []

# read through file using regex pattern to devide into match Objects
# these objects will have groups of names and speech
#  these will be put into a json file
for m in re.finditer(pattern, clean_speech_text):
    # create a dictionary then append to list for the JSON
    entry = {'surname': m.group(3), 'speech': m.group(6)}
    list_name_speech.append(entry)


# Place dicts into json format
with open('politician_and_speech.json', mode='w') as feedsjson:
    json.dump(list_name_speech, feedsjson, indent=4)
