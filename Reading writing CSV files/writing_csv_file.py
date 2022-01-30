from csv import writer ,reader, DictWriter

# writing to a csv file using writer module
#  add newline='' so that python doesn't add new line after each row
with open('results.csv','w',newline='') as file :
    write_csv = writer(file)
    # writerow expects  list of column name 
    write_csv.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    write_csv.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    write_csv.writerow(['Java', 'James Gosling', '1995', '.java'])
    write_csv.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])

# writing to a csv file using Dictwriter module
#  add newline='' so that python doesn't add new line after each row
with open('results2.csv','w',newline='') as file:
    headers = ['Name','Grade']
    write_csv = DictWriter(file,fieldnames=headers)
    write_csv.writeheader()
    write_csv.writerow({
        'Name': 'Ruman',
        'Grade': 'A+'
    })

# to get more information about any module 
# help(writer)