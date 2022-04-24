"""
    re.I => for case insensitive search
    re.VERBOSE => use for multi-line regex 
"""

import re as regex

name_regex = regex.compile(r'ruman',regex.I)
print(name_regex.findall("ruman ruMAN RUMAN RumaN"))


mail_regex = regex.compile(r'''
                \w+     # finds characters infront of @
                @
                \w+     # finds characters after @
                \.      # escape . before domain name
                \w{1,}  # detec domain com consists of minimum 1 character
                
                ''',regex.VERBOSE)

print(mail_regex.findall("ruman : ruman@gmail.com max : max123@yahoo.comf"))
