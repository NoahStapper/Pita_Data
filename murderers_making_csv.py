import json
import csv

# Doing the same thing for murderers.
data = []
first_letters = 'AHLT' # T for Ted Bundy, H for Herman Webster Mudgett, L for Lee Harvey Oswald and A for Anthony Balaam
for first_letter in first_letters: #selects every json file in the folder 
    filename = f"Filtered_data_criminals/{first_letter}_murder.json"

    with open(filename, encoding='utf8') as file:
        data = data + json.load(file) #Reads in every json file and adds it to the 'data' list

# Writing to csv files 
with open('murderers.csv', 'a', encoding='utf8') as file: #writing csv file opening function
    file.write('name,birthyear,\n')
    for datum in data: #choose whatever we want to look for
        if "ontology/birthName" in datum and "ontology/birthYear" in datum:

            file.write(f'{datum["ontology/birthName"]},{datum["ontology/birthYear"]}\n') #select what you want to put in the csv file
