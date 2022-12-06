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

class P51_data():
    def __init__(self, data, movemultiple = False):
        self.header = data[0]
        self.moves = data[1]
        self.movemultiple = movemultiple
        self.parseHeader()
        self.executeMoves()

    def parseHeader(self):
        rows = self.header.split('\n')
        lastRow = rows.pop()
        boxes = lastRow.split('   ')
        self.stack = []
        for b in boxes:
            b = b.strip()
            self.stack.append([])
        numRows = len(rows)
        i = 0
        while i < numRows:
            r = rows.pop()
            for b in boxes:
                box = r[((int(b)-1)*4)+1]
                j = int(b) - 1
                if box != ' ':
                    self.stack[int(b)-1].append(box)
            i+=1

    def moveStack(self, quantity, fromstack, tostack):
        i = 0
        fromstack = fromstack - 1
        tostack = tostack - 1
        if self.movemultiple == True:
            cratestack = []
            while i < quantity:
                i+=1
                cratestack.append(self.stack[fromstack].pop())
            i = 0
            while i < quantity: 
                self.stack[tostack].append(cratestack.pop())
                i+=1
        else:
            while i < quantity:
                i+=1
                box = self.stack[fromstack].pop()
                self.stack[tostack].append(box)

    def getCrates(self):
        crates = ''
        for s in self.stack:
            if len(s) > 0:
                crates += s[len(s)-1]
            else:
                crates += ' '
        return crates

    def executeMoves(self):
        moverows = self.moves.split('\n')
        for m in moverows:
            move_commands = m.split(' ')
            quantity = int(move_commands[1])
            stackfrom = int(move_commands[3])
            stackto = int(move_commands[5])
            self.moveStack(quantity, stackfrom, stackto)
            #print(f'{self.getCrates()}')



def problem51(part2 = False):
    data = P51_data(read_file('5-1.input').split('\n\n'), part2)
    print(f'{data.getCrates()}')

class problem61():
    def __init__(self, buffersize = 4):
        self.data = read_file('6-1.input')
        self.buffer = []
        self.buffersize = buffersize
    
    def compare_elements(self, list):
        same = False
        i = 0
        x = list.pop()
        if len(list) == 0:
            return same
        for y in list:
            same = same or (x == y)
        same = same or self.compare_elements(list.copy())
        return same
            
    def test_compare(self):
        buffer = ['a','b','c','c']
        print(self.compare_elements(buffer))

    def solve(self):
        index = 1
        for i in self.data:
            self.buffer.insert(0,i)
            if len(self.buffer) >= self.buffersize:
                print(f'{self.buffer}')
                if (self.compare_elements(self.buffer.copy()) == False):
                    return index
                self.buffer.pop()
            index += 1
        return -1
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = problem61(14)
    #x.test_compare()
    print(f'{x.solve()}')


