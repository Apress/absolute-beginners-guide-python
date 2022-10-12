#open file for reading
file = open ('data.txt' , 'r')

dataInFile = file.read()

print (dataInFile)

#close the file
file.close()
