userData = { 'ID' : 1234 ,
             'Surname' : 'Davies' ,
             'Forname' : 'Sarah' }


print( 'Reference:' , userData['ID'] )
print( 'Reference:' , userData['Surname'] )

userData['Surname'] = 'Daniels'

print( '\nReference:' , userData['ID'] )
print( 'Reference:' , userData['Surname'] )
