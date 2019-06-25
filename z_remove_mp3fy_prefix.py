import os

path = os.getcwd()
filenames = os.listdir(path)

substring = "[MP3FY.COM]"
for filename in filenames:
    if substring in filename:
        os.rename(filename, filename.replace(substring, ""))

# Remove any spaces
filenames = os.listdir(path)
for filename in filenames:
    os.rename(filename, filename.replace(" ", ""))

# Remove any quotes
filenames = os.listdir(path)
for filename in filenames:
    os.rename(filename, filename.replace("'",""))

