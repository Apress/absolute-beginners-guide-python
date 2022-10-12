#open file for reading
file = open ('data.txt' , 'r')

dataInFile = file.readline(2)

print (dataInFile)

#close the file
file.close()
