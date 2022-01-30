from csv import reader
from csv import DictReader


# with open() as file this structure is called context manager in python
# reading file using reader module
print("Reader module : ")
with open('keep.csv','r') as file :
    my_reader = reader(file)
    for row in my_reader:
        print(row)

# help(reader)
# reading file using DictReader module
print("Dictreader module : ")
with open('keep.csv','r') as file:
    my_dict_reader = DictReader(file)
    data = list(my_dict_reader)
    for row in data:
        print(f"{row['Language']} is created by {row['Creator']}")

# if csv file columns are n't comma delimeted then mention the delimeter
# because by default python assume it as comma
print("Reading | delimited csv file")
with open('keep2.csv','r') as file:
    my_reader = reader(file,delimiter = '|')
    for row in my_reader :
        print(row)