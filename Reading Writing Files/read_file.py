# file = open('story.txt')

# print(file.read())
# # after reading whole content of a file now cursor is in end of file
# # that's why it will print null 
# print(file.read())

# # move cursor at the beginning of file  then read file
# file.seek(0)
# print(file.read())

# # move cursor at first character then read file
# file.seek(1)
# print(file.read())

# # reading file line by line
# file.seek(0)
# print(file.readline())

# # reading lines then storing them inside a list
# file.seek(0)
# print(file.readlines())

# # closing file 
# if not file.closed:
#      file.close()

# more popular syntax for reading file 
# here we dont have to close file manually after reading,python does it
with open('story.txt') as file:
    data = file.read()
    print(data)