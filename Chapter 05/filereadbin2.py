import pickle

file = open("data2.dat", "rb")

data = pickle.load(file)

print (data)

file.close()
