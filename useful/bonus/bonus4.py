filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
#Strings don´t support item assignment, they are immutable

for filename in filenames:
    filename = filename.replace('.', '-', 1)  #method that returns a new modified string('.' will be changed for '-')
    print(filename)
    # 1 means: replace first occurence of '.' with '-'

    #Tuple is the immutable version of a list (instead of [], use ()]

filenames2 = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
