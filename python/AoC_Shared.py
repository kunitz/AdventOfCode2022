import os

def read_file(filename):
    current_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
    filename_fullpath = os.path.join(current_dir, filename)
    #print(f'{filename_fullpath}')
    # open file in read mode
    file = open(filename_fullpath, "r")

    # read whole file to a string
    data = file.read()
    #print(f'{data}')
    # close file
    file.close()
    return data
