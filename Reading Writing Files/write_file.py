# differen file modes
# r - reading mode, if file doesn't exit it throws error
# r+ - reading and writing mode, if file doesn't exit it throws error
# w - writing mode, if file doesn't exit it doesn't throw error
# a - writing content at end of file, if file doesn't exit it doesn't throw error

# override file content 
with open ('lol.txt','w') as file :
    file.write('Helloooooo!')

# append to file existing content
with open ('lol.txt','a') as file :
    file.write("\n world")

# reading and writing together
with open('together.txt','r+') as file :
    data = file.readline()
    # after reading one line now cursor is at second line
    # now write Good Bye there
    file.write("\n Good Bye")




