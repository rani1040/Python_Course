# open the file in read mode
file_read = open('Sample_File.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Sample_File.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am a class 8 student from Pune")
file_write.close()

# open the file in append mode
file_append = open('Sample_File.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! My favourite subject is Mathematics")
file_append.close()

#open file and read its contents
file = open('Sample_File.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('Sample_File.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#read first line of file
file = open('Sample_File.txt','r')
print("\n Reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('Sample_File.txt','r')
print("\n Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('Sample_File.txt','r')
print("\n Looping through the lines...")
for line in file:
  print(line)
file.close()

# write in file using with()function
with open('Sample_File', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# split file into words
with open('Sample_File.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("My_file.txt"):
  print("File exists")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("My_file.txt", "w")
my_file.write("Hi! I am Penguin. I am in class 8 studying in Pune.")
my_file.close()

#delete file named codingal
os.remove('Sample_doc.txt')
