# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_file(filename):
    current_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
    filename_fullpath = os.path.join(current_dir, filename)
    #print(f'{filename_fullpath}')
    # open text file in read mode
    text_file = open(filename_fullpath, "r")

    # read whole file to a string
    data = text_file.read()
    #print(f'{data}')
    # close file
    text_file.close()
    return data

def p41_getrange(assignmentrange1 , assignmentrange2):
    range1 = assignmentrange1.split('-')
    range2 = assignmentrange2.split('-')
    if (int(range1[0]) >= int(range2[0])) and (int(range1[1]) <= int(range2[1])):
        return 1

def p42_getoverlap(assignmentrange1, assignmentrange2):
    range1 = assignmentrange1.split('-')
    range2 = assignmentrange2.split('-')
    if (int(range1[0]) >= int(range2[0])) and (int(range1[0]) <= int(range2[1])) or (int(range1[1]) >= int(range2[0])) and (int(range1[1]) <= int(range2[1])):
        return 1

def problem41():
    data = read_file('4-1')
    count = 0
    datalist = data.split('\n')
    for row in datalist:
        assignments = row.split(',')
        if (p41_getrange(assignments[0],assignments[1])==1) or (p41_getrange(assignments[1],assignments[0])==1):
            count += 1
            #print(f'{row}')
    print(f'{count}')

def problem42():
    data = read_file('4-1')
    count = 0
    datalist = data.split('\n')
    for row in datalist:
        assignments = row.split(',')
        if (p42_getoverlap(assignments[0],assignments[1])==1) or (p41_getrange(assignments[1],assignments[0])==1):
            count += 1
            print(f'{row}')
    print(f'{count}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem42()


