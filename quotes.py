# single quote (solves problem using backslash(\) or double quote(""))
message1 = 'Life isn\'t a bed of roses'
message1 = "Life isn't a bed or roses"

# double quote (solves problem using backslash(\) or single quote(''))
message2 = "Masum said, \"Hurry up \" "
message2 = 'Masum said, "Hurry up" '

# triple quotes allow us to write both single and double quote
# triple quotes are called docstring
message3 = ''' Life isn't a bed of roses.Masum Said , "Hurry up" '''
message4 = """ Life isn't a bed of roses.Masum Said , "Hurry up" """
print(message3)
print(message4)