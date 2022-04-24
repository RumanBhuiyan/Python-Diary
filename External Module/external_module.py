# for gethering information about an external packages
# open cmd and import the package then help(package_name)
# termcolor helps to print colored text in output terminal
# pyfiglet  helps to generate ASCII art for any string
# autopep8  --in-place -a -a file_name
# autopep8 formats python code , --in-place flag replace changes in original file
# -a means aggressive & 2 times -a flag changes all if condition==True to if condition

from termcolor import colored
from pyfiglet import figlet_format


user_text = input("Enter your text : ")
ascii_text = figlet_format(user_text)
colored_text = colored(ascii_text, color='red', on_color='on_green')

# print(help(termcolor))
print(colored_text)

# install package recent version: pip install package_name  
# install package specific verstion: pip install package_name==3.0.5
