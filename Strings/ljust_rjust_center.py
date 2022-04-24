"""
    string.ljust(length) make string left justified then takes length in including provided string
                            and keep blank spaces as it is
    string.ljust(length,'=') make string left justified then takes length in including provided string
                            and fill up blank spaces by = 
    
    string.rjust(length) make string right justified then takes length in including provided string
                            and keep blank spaces as it is
    string.rjust(length,'=') make string right justified then takes length in including provided string
                            and fill up blank spaces by = 
    
    string.center(length) align string in center 
    string.center(length, '=') align string in center and fill up blank spaces with =
"""

name = "Ruman"

print(name.ljust(20))
print(name.ljust(20,'='))

print(name.rjust(20))
print(name.rjust(20,'='))

print(name.center(20))
print(name.center(20,'='))
