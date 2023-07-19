import os
import shutil

for file in os.listdir(os.getcwd()):
    if file != 'main.py':
        extension=os.path.splitext(file)
        extension=extension[-1]
        try:
            if not os.path.isdir(extension):
                os.makedirs(extension)
        except Exception as e:
            if not os.path.isdir('Others'):
                os.makedirs('Others')

for file in os.listdir(os.getcwd()):
    if file != 'main.py' and file[0] != '.':
        extension=os.path.splitext(file)
        extension=extension[-1]
        try:
            shutil.move(file, extension)
        except Exception as e:
            shutil.move(file, 'Others')