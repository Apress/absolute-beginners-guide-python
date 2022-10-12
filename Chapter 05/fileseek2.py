#open file for reading
file = open ('data3.txt' , 'w')

i=0
for i in range(0,8): #range 0 to 7
    file.write ("*")
file.write("\n")

i=0
position=17
for i in range(0,8):
    file.write("*")
    file.seek(position)
    file.write("*")
    file.write("\n")
    position+=10

i=0
for i in range(0,8):
    file.write ("*")

    
#close the file
file.close()
