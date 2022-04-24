# N.B => run this python program in linux envrionment or WSL to get proper output and better understanding

# subprocess helps us to run terminal/system command from our python program
# few methods and features dont work in windows like below
import subprocess

# process - 01 : run the command in terminal but dont capture that command output
# shell = True makes shell interactive at the time of executing python program
result1 = subprocess.call(['date'],shell=True)
result2 = subprocess.run(['ls', '-a'])

# process - 02 : run the command in terminal and capture that command output
result3 = subprocess.run(['echo','hello'],capture_output=True)
print(result3)
# print(result2)
# print(result2.returncode)

