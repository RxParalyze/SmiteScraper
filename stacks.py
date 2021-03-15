import json
import urllib.request
import re
import tensorflow as tf

with open('items_result.json') as f:
    data = json.load(f)

items = []

sourceItems = data

stacksDict = [
    "max",
    "up to"
]

typeDict = [
    "Attack Speed",
    "Basic Attack Power",
    "Cooldown Reduction",
    "Critical Chance",
    "Critical Damage",
    "Health",
    "HP5",
    "Magical Lifesteal",
    "Magical Protection",
    "Magical Power",
    "Mana",
    "Movement Speed",
    "MP5",
    "Penetration Chance",
    "Penetration Power",
    "Physical Lifesteal",
    "Physical Power",
    "Physical Protection"
]

for sourceItem in sourceItems:
    if "passive" in sourceItem:
        for phrase in stacksDict:
            if phrase in sourceItem['passive'].lower():
                print(sourceItem['name'] + ": {}".format(phrase))
                for category in typeDict:
                    print(sourceItem['name'] + ": {}".format(category))
                    if category in sourceItem['passive'].lower():
                        print(sourceItem['name'] + ": {}".format(category))
                        #amount = re.findall(r'\d+', basicAttackFlatIncrease.group())
                        amount = re.findall(r'\d+')
                        sourceItem['stacks']['stacks'][("{}".format(category))]['amount'] = amount
                        continue
                continue
    items.append(sourceItem)

with open('items_result.json', 'w') as json_file:
    json.dump(items, json_file, indent='\t', sort_keys=True)