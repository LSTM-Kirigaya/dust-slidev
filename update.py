import os
import json


with open('index.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

for item in data['content']:
    folder = item['path']
    os.system('python mySlidev.py --build --update -i ' + folder)