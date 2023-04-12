import glob  # dealing with multiple files

# * means everything that has .txt

myFiles = glob.glob("../filesCodeExperiments/*.txt")  # glob is the module, glob() is the function of the module.
# returns a list of all the filepaths

for filepath in myFiles:  # iterating through a list of files
    with open(filepath, 'r') as file:  # opening each file inside myFiles list(glob function returned it)
        print(file.read())  # printing file.read() (text content inside the file.)

