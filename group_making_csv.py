import json
import csv

data = []
first_letters = 'TGRO' # T for Theodore, G for Grover, R for Richard and O for Ronald
for first_letter in first_letters: #selects every json file in the folder 
    #print(f'{first_letter}')
    filename = f'{first_letter}_name.json'

    with open(filename, encoding='utf8') as file:
        data = json.load(file) #gives you a list of dictionaries

    with open('presidents.csv', 'a', encoding='utf8') as file: #writing csv file opening function
        #file.write('name,\n')
        for datum in data: #choose whatever we want to look for
            #first_name = datum["ontology/birthName"]
            if "ontology/birthName" in datum and "ontology/birthYear" in datum: #and datum[first_name] == "Theodore": #If label is existing key, and corresponding value is country name, add to results list
                #if datum["ontology/birthYear"] == 
                #if "ontology/birthName" in datum and "Theodore" in datum["ontology/birthName"]:
                #print(datum["ontology/birthName"])

                    file.write(f'{datum["ontology/birthName"]},{datum["ontology/birthYear"]}\n') #select what you want to put in the csv file



#with open('all_names.csv', 'a', encoding='utf8') as file: #writing csv file opening function