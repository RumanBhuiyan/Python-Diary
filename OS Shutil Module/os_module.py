import os


print(f'My Operating system name : {os.environ["OS"]}')
print(f'Os Environment Information : {os.environ}')

print (f'Current working directory : {os.getcwd()}')

# chdir -> change directory
os.chdir('C:\\Users\\DSI\\Downloads\\Keep')
print (f'Now Current working directory : {os.getcwd()}')

os.mkdir('Test_notes') # create a folder named 'Test_notes'
os.makedirs('Notes\\notes1') # create 2 folder in Notes/notes1 this path
print(f'Folder inside current directory : {os.listdir()}') # listdir() shows all available directories


#os.remove('Sample.txt') # remove a sinle file 
os.rmdir('Test_notes') # remove empty directory
os.removedirs('Notes\\notes1') # remove also nested folders
print(f'Available folders : {os.listdir()}')

#os.rename('Test.txt','Sample.txt') #rename file

# os.stat() used for getting file informations like size,modification time etc
print(os.stat('Sample.txt')) 


# lets explore os.path
print(f'Sample.txt exists ? : {os.path.exists("Sample.txt")}')
print(f'Size of Sample.txt : {os.path.getsize("Sample.txt")} Bytes')

# os.path.join() can be used for creating new path combining two path