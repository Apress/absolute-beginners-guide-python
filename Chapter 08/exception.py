try:
  file = open("file.txt", "r")
  data = file.read()
  print (data)
  file.close() 
except (FileNotFoundError):
  print("File not found")
