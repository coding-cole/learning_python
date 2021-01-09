# # creat a file
# myfile = open("fruits.txt")

# # read file
# content = myfile.read()

# # close file
# myfile.close

# always use the 'with' context manager
# always use "r" to indicate the read mode or "w if write"
with open("files/fruits.txt", "r") as myfile:
    content = myfile.read()

# create a file with the "w" and write into the file with file.write()
# "x" cannot overite an existing file 
# "a" is used to append to a file
# "a+" is used to read and write a file
# use file.seek(0) to set cpooursor to begging of file
with open("files/vegetables", "a+") as yourfile:
    yourfile.write("\nOkro")
    yourfile.seek(3)
    yourfcontent = yourfile.read()

print(yourfcontent)
