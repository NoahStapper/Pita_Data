#Welcome Pita data people

#Loading json files
import json
# import csv

# variable names
keys_potential_country = ["ontology/country_label", "ontology/nationality_label"]
country = "United Kingdom"

# Loading the json data

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #remember to add the rest of the letters at the start of json files
for letter in letters: #selects every json file in the folder
    filename = f'{letter}_people.json'

    with open(filename, encoding='utf8') as file:
        data = json.load(file) #gives you a list of dictionaries

        with open('people.csv', 'a', encoding='utf8') as file: #writing csv file opening function
            for datum in data: #choose whatever we want to look for
                for key in keys_potential_country:
                    if key in datum and country in datum[key]: #If label is existing key, and corresponding value is country name, add to results list
                        if "ontology/deathCause_label" in datum:
                            print(datum["ontology/deathCause_label"])
                            #for label in labels:

                        break
                            
                
               # if "ontology/country_label" in datum or "ontology/nationality_label" in datum: # and "ontology/deathCause_label" in datum
                #    if datum["ontology/country_label"] == "United Kingdom" or datum["ontology/nationality_label"] == "United Kingdom": #and datum["ontology/deathCause_label"] == "suicide":
                 #       print(datum["ontology/deathCause_label"])
                    #print(datum["ontology/country_label"] or datum["ontology/nationality_label"])

                        file.write(f'{datum[label]}\n') #select what you want to put in the csv file
          
        