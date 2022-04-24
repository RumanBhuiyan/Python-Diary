"""
    re.sub() helps us to substitute a string found by regex
"""
import re as regex

# process - 01
facebook = "facebook is a popular social medaia and many peoples are addicted in facebook"
print(facebook)

facebook = regex.sub("[fF]acebook","Meta", facebook)
print(facebook)

# process - 02
facebook = "facebook is a popular social medaia and many peoples are addicted in facebook"

replace_facebook = regex.compile(f'[fF]acebook')
facebook = replace_facebook.sub("Meta",facebook)
print(facebook)