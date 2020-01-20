#Welcome Pita data people

#Loading json files
import json
# import csv

# Loading the json data

letters = 'ABCDEFG' 
for letter in letters: #selects every json file in the folder
    filename = f'{letter}_people.json'

    with open(filename, encoding='utf8') as file:
        data = json.load(file) #gives you a list of dictionaries

        with open('people.csv', 'a', encoding='utf8') as file: #writing csv file opening function
            for datum in data: #choose whatever we want to look for
                if "ontology/country_label" in datum and "ontology/birthYear" in datum:
                    if datum["ontology/country_label"] == "United Kingdom" and datum["ontology/birthYear"] == "1944":
                        print(datum["title"])

                        file.write(f'{datum["title"]}\n') #select what you want to put in the csv file
          
        