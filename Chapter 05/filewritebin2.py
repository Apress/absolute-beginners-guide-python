import pickle

file = open("data2.dat", "ab")

mailing = []



pickle.dump(mailing, file)

file.close()
