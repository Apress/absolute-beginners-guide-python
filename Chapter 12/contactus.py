#!/python/python

import cgi, smtplib

# Create form object
form = cgi.FieldStorage()

# Get data from form fields
name = form.getvalue("name")
email = form.getvalue("email")
message = form.getvalue("message")

# Generate response page
print ('Content-type:text/html\r\n\r\n')
print ('<!doctype html>')
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>Contact Us</title>')
print ('</head>')
print ('<body>')
print ('<h2>Contact Us</h2>')
print ('<p>Thanks', name, ' for your message.</p>')
print ('<p>This is what you sent:</p>')
print (message)
print ('</body>')
print ('</html>')

# Construct email message
