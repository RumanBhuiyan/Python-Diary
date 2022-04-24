import re as regex

# step -01 : import regex 
# step -02 : compile regex pattern as raw string to get a regex object
# step -03 : in that object you will have the access to .search() which will store all matches
# step -04 : .group() will return all matches as tuple
phone_number_regex = regex.compile(r'\d{3}-\d{3}-\d{4}')
matched = phone_number_regex.search('phone1 : 123-231-2232 phone2 : 465-654-1234')

# group() returns the default group no 0
# if you create group using () in your regex pattern then you can also get group(0) from match
print(matched)
print(matched.group())