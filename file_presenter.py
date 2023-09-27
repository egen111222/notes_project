# READ
# WRITE

import pickle
import os

def read_form_file(filename):
    with open(filename,"rb") as file:
        return pickle.loads(file.read())


def write_to_file(filename,data):
    with open(filename,"wb") as file:
        file.write(pickle.dumps(data))


def check_file(filename):
    if not os.path.exists(filename):
        write_to_file(filename,[])
