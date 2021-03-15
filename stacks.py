import json
import urllib.request
import re

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
    "Magical Defense",
    "Magical Lifesteal",
    "Magical Power",
    "Mana",
    "Movement Speed",
    "MP5",
    "Penetration Chance",
    "Penetration Power",
    "Physical Defense",
    "Physical Lifesteal",
    "Physical Power"
]

for sourceItem in sourceItems:
    for phrase in stacksDict:
        if phrase in sourceItem['passive']:
            for category in typeDict:
                if category in sourceItem['passive']:
                    #amount = re.findall(r'\d+', basicAttackFlatIncrease.group())
                    amount = re.findall(r'\d+')
                    sourceItem['stacks']['stacks'][category]['amount'] = amount
                    break
            break

with open('items_result.json', 'w') as json_file:
    json.dump(items, json_file, indent='\t', sort_keys=True)