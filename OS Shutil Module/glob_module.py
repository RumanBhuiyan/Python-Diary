from glob import glob

python_files = glob('./*.py')
txt_files = glob('./**/*.txt',recursive=True)

print(f'{len(python_files)} python files found')
print(f'Files are {python_files}')

print(f'{len(txt_files)} txt files found')
print(f'Files are {txt_files}')