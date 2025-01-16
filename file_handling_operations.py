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

#read first line of file
file = open('Codingal.txt','r')
print("Reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('Codingal.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('Codingal.txt','r')
print("Looping through the lines...")
for line in file:
  print(line)
file.close()

# Program to remove lines starting with any prefix

file1 = open('Codingal.txt',
			'r')
file2 = open('CodingalUpdated.txt',
			'w')

# reading each line from original
# text file
for line in file1.readlines():
	
	# reading all lines that do not
	# begin with "Coding"
	if not (line.startswith('Coding')):
		
		# printing those lines
		print(line)
		
		# storing only those lines that
		# do not begin with "Coding"
		file2.write(line)

# close and save the files
file2.close()
file1.close()
