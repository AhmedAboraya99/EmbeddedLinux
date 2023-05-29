import csv

Data = csv.reader(open("names.csv", "r"))
for row in Data:
    print(row)
    print(len(row))
    
dict_1 = {}
for line in Data:
    dict_1[line[0]] = {'name' : line[1], 'age' : line[2] }

print(dict_1)