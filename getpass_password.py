from getpass import getpass

username = input('Username : ')
password = getpass('Password : ')

print('Logging in.........')
# if we use getpass() instead of input() then user typing contents are invisible
#  in terminal