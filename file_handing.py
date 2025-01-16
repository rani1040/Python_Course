# open file and store file object in a variable
file = open('Codingal.txt')

# read the contents of file
print(file.read())

# close the file
file.close()


#open file and read its contents
file = open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('Codingal.txt','a')
file.write(" Hi! I am Penguin and I am 1 yr old.")
file.close()

# open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()

