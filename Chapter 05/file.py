#get some information
username = input('Enter your name: ')
useremail = input('Enter your email: ')


#open file for writing
file = open( 'data.txt' , 'a' )


#write the data to the file data.txt
file.writelines (username)
file.writelines (' ') #add space between
file.writelines (useremail)


#close the file
file.close()
