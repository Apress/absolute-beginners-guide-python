import pickle

file = open("data.dat", "wb")

text = "This is text to be written to the file...!"

pickle.dump(text, file)

file.close()
