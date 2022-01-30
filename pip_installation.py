# Checking version (add python/scripts to your path so that cmd can find pip.exe)

# python3 -m pip --version
# python2 -m pip --version

#Here at first we specified python version then imported that version pip



# checking all installed packages list

# python3 -m pip list
# python2 -m pip list



# installing a package for python2 and python3 

# python3 -m pip install heroes
# python2 -m pip install heroes

# if we have only one version of python installed in my computer then those command
# can be simplified as 'pip list heroes' but at the time of working with different 
# versions of python we have to work with pip in this manner.


# checking outdated versions and updating

# pip list --outdated or pip list -o   (show all packages that dont have updated version)
# pip install -U <package_name> (install the updated version of the package)


# installing all packages mentioned in requirements.txt

# pip install -r requirements.txt (install all packages mentioned in requirements.txt)