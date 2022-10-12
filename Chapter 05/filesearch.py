#get some information
searchterm = input('Enter your search')

#open file for reading
file = open ('data.txt' , 'r')

linenumber = int(1)

# Check line-by-line if string is in data.txt
for line in file:
        if searchterm in line:
                print ("String found on line", linenumber)
                print (line)
        linenumber = linenumber + 1

#close the file
file.close()
