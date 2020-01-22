import json
import csv

# Reading in the json files
data = []
first_letters = 'TGRO' # T for Theodore, G for Grover, R for Richard and O for Ronald
for first_letter in first_letters: #selects every json file in the folder 
    filename = f"Filtered_data_presidents/{first_letter}_name.json"

    with open(filename, encoding='utf8') as file:
        data = data + json.load(file) #Reads in every json file and adds it to the 'data' list

# Writing to csv files 
with open('presidents.csv', 'a', encoding='utf8') as file: #writing csv file opening function
    file.write('name,birthyear,\n')
    for datum in data: #choose whatever we want to look for
        if "ontology/birthName" in datum and "ontology/birthYear" in datum:

            file.write(f'{datum["ontology/birthName"]},{datum["ontology/birthYear"]}\n') #select what you want to put in the csv file

# Making headers for external dataset to code in R
# with open('Perf_Pres.csv') as csvDataFile:
#     with open('perf_presidents.csv', 'w', encoding='utf8') as csv: #writing csv file opening function
#         csv.write('xx,name,percentage,\n')
#         for row in csvDataFile:
#             csv.write(f"{row}")
