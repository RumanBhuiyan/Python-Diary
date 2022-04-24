names  = ['Ruman','Robiul','Parbez','Shahadat']
rolls =  [76,79,88,26]


names_rols  = list(zip(names,rolls))
print(names_rols) # [('Ruman', 76), ('Robiul', 79), ('Parbez', 88), ('Shahadat', 26)]


names_rols = dict(zip(names,rolls))
print(names_rols) # {'Ruman': 76, 'Robiul': 79, 'Parbez': 88, 'Shahadat': 26}s


# lets look an example of zip and tuple unpacking
for name,roll in zip(names,rolls):
    print(f'name : {name} registration no : {roll}')
