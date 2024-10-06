import os 
directory_path = '/All Files'
contents = os.listdir(directory_path)
for item in contents: 
    print(item)
