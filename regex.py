# you can check your regex here: https://pythex.org/
import re as regex

pattern = regex.compile(r'^\d{10}$')
registration_number  = input()

if pattern.match(registration_number):
    print("Valid registration number")
else :
    print("Invalid registration number")

# print(pattern.search(registration_number))
# print(pattern.match(registration_number))
# print(pattern.findall(registration_number))