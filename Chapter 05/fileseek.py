#open file for reading
file = open ('data.txt' , 'r')

#move pointer to the 6th character in the file
file.seek (5)

#read line in file starting from 6th character
dataInFile = file.readline()

print (dataInFile)


#close the file
file.close()
