# process : 01 (creating own context manager using class)
class open_my_file:

    # this method is called at the time of open_my_file('context_class.txt','w')
    def __init__(self,filename,filemode) :
        self.filename = filename
        self.filemode = filemode

    # returning value is assigned to my_file to use inside context    
    def __enter__(self):
        self.file = open(self.filename,self.filemode)
        return self.file
    
    # when my_file goes out of indentation then this method is called automatically
    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()


with open_my_file('context_class.txt','w') as my_file:
    my_file.write('context class contents...')


# lets check whether files closed or not
print(f'my_file closed ? : {my_file.closed}')