import os
import shutil

def group_files_by_name(directory):
    os.chdir(directory)


    files_dict = {}


    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            name, ext = os.path.splitext(filename)
            # Group by name, ignoring the extension
            if name not in files_dict:
                files_dict[name] = []
            files_dict[name].append(filename)


    for name, files in files_dict.items():
        if not os.path.exists(name):
            os.makedirs(name)
        

        for file in files:
            shutil.move(file, os.path.join(name, file))


directory = '/your/directory/here/'  # Replace with your directory path
group_files_by_name(directory)