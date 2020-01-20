#Welcome Pita data people

#Loading json files
import json

# Loading the json data
with open('A_people.json', encoding='utf8') as file:
    data = json.load(file) # gives you a list of dictionaries