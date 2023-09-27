# READ
# WRITE

import pickle


def read_form_file(filename):
    with open(filename,"rb") as file:
        return pickle.loads(file.read())


def write_to_file(filename,data):
    with open(filename,"wb") as file:
        file.write(pickle.dumps(data))
