import pickle

file = open("data.dat", "rb")

data = pickle.load(file)

print (data)

file.close()
