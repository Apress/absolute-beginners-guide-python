# Errata for *The Absolute Beginner's Guide to Python Programming*

On **page 44** [Program code]:
 
Last three lines "using the and operator..." are not part of the program.

***

On **page 70** ["writing" should be "reading"]:
 
When opening a file for **reading**, use either of the following...

***

On **page 81** [no .read() method, should be .load()]:
 
In binary file operations, to read a file, use the **pickle.load()** method. Use: **pickle.load(file-name-to-read-from)**

***

On **page 111** [init method missing double underscores]:
 
Line should be: def &#95;&#95;init&#95;&#95;(self, name, dob, email):

***

On **page 114** [super() function allows access to parent methods]:
 
When defining your child classes, you might need to access methods defined in the parent. To do this, use the super() function. The super() function allows us to refer to the parent class explicitly.

***
