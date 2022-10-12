number = input("Enter a positive number: ")

if int(number) < 0:
  raise ValueError ("Negative numbers are now allowed.")
