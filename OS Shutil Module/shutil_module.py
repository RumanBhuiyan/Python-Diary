# article : https://www.askpython.com/python-modules/shutil-module
import shutil


# copy the content of 'sample.txt' to 'sample2.txt' without copying metadata
shutil.copy('sample.txt','sample2.txt')

# copy file content & metadata(file creation time,modification time etc) both
shutil.copy2('sample.txt','sample2.txt')

# copying file inside a folder (without metadata)
shutil.copyfile('sample.txt','Notes\\test.txt')


# moving files
shutil.move('sample2.txt','Notes')

#copying folders & files recursively 
shutil.copytree('Notes','Notes2') 

# removing files & folders recursively
shutil.rmtree('Notes2')