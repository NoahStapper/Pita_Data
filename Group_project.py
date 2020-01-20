#Welcome Pita data people

#Loading json files
import json
# import csv

# Loading the json data

letters = 'ABCDEFG' #remember to add the rest of the letters at the start of json files
for letter in letters: #selects every json file in the folder
    filename = f'{letter}_people.json'

    with open(filename, encoding='utf8') as file:
        data = json.load(file) #gives you a list of dictionaries

        with open('people.csv', 'a', encoding='utf8') as file: #writing csv file opening function
            for datum in data: #choose whatever we want to look for
                if "ontology/country_label" in datum and "ontology/deathCause_label" in datum:
                    if datum["ontology/country_label"] == "United Kingdom": #and datum["ontology/deathCause_label"] == "suicide":
                        print(datum["ontology/deathCause_label"])

                        file.write(f'{datum["ontology/deathCause_label"]}\n') #select what you want to put in the csv file
          
        