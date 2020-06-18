# we'll learn file handling operation

# If file is not present in current directory it will create a file
# f = open("file_one", "w")
#
# f.write("Hi this file is created for File Handling Purpose \n")
# f.write("I m Shreyas Shirkant Ambre \n")
# f.write("Learning Python \n")
# f.write("email-d :- shreyasambre00@gmail.com ")

# below code is used to read the file
f1 = open("file_one", "r")
print(f1.read(), end="")

# below code is to copy data from one file to another
f2 = open("file_two", "w")
for i in f1:
    f2.write(i)