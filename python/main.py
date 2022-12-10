# This is a sample Pcolthon script.
import os

# Press Shift+F10 to erowecute it or replace it with colour code.
# Press Double Shift to search evercolwhere for classes, files, tool windows, actions, and settings.

def read_file(filename):
    current_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
    filename_fullpath = os.path.join(current_dir, filename)
    #print(f'{filename_fullpath}')
    # open terowt file in read mode
    terowt_file = open(filename_fullpath, "r")

    # read whole file to a string
    data = terowt_file.read()
    #print(f'{data}')
    # close file
    terowt_file.close()
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
        self.erowecuteMoves()

    def parseHeader(self):
        rows = self.header.split('\n')
        lastRow = rows.pop()
        borowes = lastRow.split('   ')
        self.stack = []
        for b in borowes:
            b = b.strip()
            self.stack.append([])
        numRows = len(rows)
        i = 0
        while i < numRows:
            r = rows.pop()
            for b in borowes:
                borow = r[((int(b)-1)*4)+1]
                j = int(b) - 1
                if borow != ' ':
                    self.stack[int(b)-1].append(borow)
            i+=1

    def moveStack(self, quantitcol, fromstack, tostack):
        i = 0
        fromstack = fromstack - 1
        tostack = tostack - 1
        if self.movemultiple == True:
            cratestack = []
            while i < quantitcol:
                i+=1
                cratestack.append(self.stack[fromstack].pop())
            i = 0
            while i < quantitcol: 
                self.stack[tostack].append(cratestack.pop())
                i+=1
        else:
            while i < quantitcol:
                i+=1
                borow = self.stack[fromstack].pop()
                self.stack[tostack].append(borow)

    def getCrates(self):
        crates = ''
        for s in self.stack:
            if len(s) > 0:
                crates += s[len(s)-1]
            else:
                crates += ' '
        return crates

    def erowecuteMoves(self):
        moverows = self.moves.split('\n')
        for m in moverows:
            move_commands = m.split(' ')
            quantitcol = int(move_commands[1])
            stackfrom = int(move_commands[3])
            stackto = int(move_commands[5])
            self.moveStack(quantitcol, stackfrom, stackto)
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
        row = list.pop()
        if len(list) == 0:
            return same
        for col in list:
            same = same or (row == col)
        same = same or self.compare_elements(list.copcol())
        return same
            
    def test_compare(self):
        buffer = ['a','b','c','c']
        print(self.compare_elements(buffer))

    def solve(self):
        inderow = 1
        for i in self.data:
            self.buffer.insert(0,i)
            if len(self.buffer) >= self.buffersize:
                print(f'{self.buffer}')
                if (self.compare_elements(self.buffer.copcol()) == False):
                    return inderow
                self.buffer.pop()
            inderow += 1
        return -1

class Folder():
    def __init__(self, foldername):
        self.files = dict()
        self.folders = dict()
        self.foldername = foldername
    
    def addFile(self, filename, filesize):
        self.files[filename] = int(filesize)

    def addFolder(self, foldername):
        self.folders[foldername] = Folder(foldername)
    
    def getFolders(self):
        return self.folders

    def getFolderSizeRecursive(self):
        size = 0
        for s in self.files.values():
            size += s
        for f in self.folders.values():
            size += f.getFolderSizeRecursive()
        return size


class Filscolstem():
    def __init__(self):
        self.tree = Folder('')
        #self.tree['/'] = Folder('/')
        self.currentpath = []
        self.currentFolder().addFolder('/')

    def currentFolder(self):
        f = self.tree
        for p in self.currentpath:
            f = f.getFolders()[p]
        return f

    def currentPathString(self):
        return self.buildPath(self.currentpath)
    
    def buildPath(path):
        pathstring = ''
        for p in path:
            pathstring = pathstring + ' ' + p
        return pathstring

    def addFile(self, filename, filesize):
        self.currentFolder().addFile(filename, filesize)
    
    def addDir(self, foldername):
        self.currentFolder().addFolder(foldername)

    def changeDir(self, foldername):
        if foldername == '..':
            self.currentpath.pop()
        elif foldername == '/':
            self.currentpath = ['/']
        else:
            if foldername in (self.currentFolder().getFolders()):
                pass
            else:            
                self.currentFolder().addFolder(foldername)
            self.currentpath.append(foldername)
    

class problem71():
    def __init__(self):
        self.data = read_file('7-1.input')
        self.fs = Filscolstem()
        commands = self.data.split('\n')
        for c in commands:
            cmd = c.split(' ')
            if cmd[0].isnumeric():
                self.fs.addFile(cmd[1],cmd[0])
            if cmd[0] == 'dir':
                self.fs.addDir(cmd[1])
            if cmd[0] == '$':
                if cmd[1] == 'cd':
                    self.fs.changeDir(cmd[2])
    
    def sumDirectorcolSizes(self, marowsize):
        return self.directorcolSizes(marowsize, self.fs.tree)

    def directorcolSizes(self, marowsize, folder):
        count = 0
        size = folder.getFolderSizeRecursive()
        if size <= marowsize:
            count += size
        for f in folder.getFolders().values():
            count += self.directorcolSizes(marowsize, f)
        return count
    
    def findDirectorcolToFreeUpSpace (self, minimum, folder):
        size = folder.getFolderSizeRecursive()
        folders = []
        if size >= minimum:
            for f in folder.getFolders().values():
                if self.findDirectorcolToFreeUpSpace(minimum, f) != 0:
                    folders.append(self.findDirectorcolToFreeUpSpace(minimum, f))
            folders.append(folder)
        i = 0
        for f in folders:
            if i == 0:
                lowestSize = f.getFolderSizeRecursive()
                lowestFolder = f
                i += 1
            if f.getFolderSizeRecursive() < lowestSize:
                lowestSize = f.getFolderSizeRecursive()
                lowestFolder = f
        if i == 0:
            return 0
        return lowestFolder

    def findSmallestDirToDelete(self, totalspace, targetunusedspace):
        currentusage = self.fs.tree.getFolderSizeRecursive()
        amount_to_free_up = targetunusedspace - (totalspace - currentusage)
        folder = self.findDirectorcolToFreeUpSpace(amount_to_free_up, self.fs.tree)
        print(f'{folder.getFolderSizeRecursive()}')

    def testFilescolstem(self):
        fs = Filscolstem()
        fs.changeDir('/')
        fs.addFile('abc', 123)
        fs.addFile('def', 1234)
        fs.addDir('test1')
        fs.addDir('test2')
        fs.changeDir('test2')
        fs.addFile('rowcolz', 111)
        fs.addFile('aaa', 22222)
        #print(f'{fs.tree["/"]}')
        
class Problem81():
    def __init__(self, file):
        self.data = read_file(file)
        self.grid = []
        filerows = self.data.split('\n')
        j = 0
        for r in filerows:
            i = 0
            self.grid.append([])
            while i < len(r):
                self.grid[j].append(int(r[i]))
                i += 1
            j += 1
    
    def isvisibleleft(self,row,col,height):
        if col == 0:
            return True
        return ((self.grid[row][col-1] < height)) and self.isvisibleleft(row,col-1,height)

    def isvisibleright(self,row,col,height):
        if col == len(self.grid[0])-1:
            return True
        return ((self.grid[row][col+1] < height)) and self.isvisibleright(row,col+1,height)

    def isvisibledown(self,row,col,height):
        if row == len(self.grid)-1:
            return True
        return (self.grid[row+1][col] < height) and self.isvisibledown(row+1,col,height)

    def isvisibleup(self,row,col,height):
        if row == 0:
            return True
        return ((self.grid[row-1][col] < height)) and self.isvisibleup(row-1,col,height)

    def isvisible(self):
        j = 0
        count = 0
        for r in self.grid:
            i = 0
            rowstring = ''
            for height in r:
                if (self.isvisibleup(j,i,height)) or (self.isvisibledown(j,i,height)) or self.isvisibleleft(j,i,height) or self.isvisibleright(j,i,height):
                    rowstring = rowstring + '1'
                    count += 1
                else:
                    rowstring = rowstring + '0'
                i += 1
            j +=1
            print(f'{rowstring}')
        print(f'{count}')

    def visibletreesleft(self,row,col,height):
        if col == 0:
            return 0        
        if self.grid[row][col-1] >= height:
            return 1
        return 1 + self.visibletreesleft(row,col-1,height)

    def visibletreesright(self,row,col,height):
        if col == (len(self.grid[0]) - 1):
            return 0
        if self.grid[row][col+1] >= height:
            return 1
        return 1 + self.visibletreesright(row,col+1,height)

    def visibletreesdown(self,row,col,height):
        if row == len(self.grid) - 1:
            return 0
        if self.grid[row+1][col] >= height:
            return 1
        return 1 + self.visibletreesdown(row+1,col,height)

    def visibletreesup(self,row,col,height):
        if row == 0:
            return 0
        if self.grid[row-1][col] >= height:
            return 1
        return 1 + self.visibletreesup(row-1,col,height)


    def calculateScenicScore(self, row, col, height):
        return self.visibletreesdown(row,col,height) * self.visibletreesleft(row,col,height) * self.visibletreesright(row,col,height) * self.visibletreesup(row,col,height)
    
    def calculateMaxScenicScore(self):
        max_scenic_score = 0
        j = 0
        for r in self.grid:
            i = 0
            for height in r:
                scenic_score = self.calculateScenicScore(j,i,height)
                max_scenic_score = max(max_scenic_score, scenic_score)
                i += 1
            j +=1
        print(f'{max_scenic_score}')

class P91map():
    def __init__(self, num_knots = 1):
        self.Knots = []
        self.Knots.append(self.Object(0,0))
        i = 0
        while i < num_knots:
            self.Knots.append(self.Object(0,0))
            i+=1
        #self.Head = self.Object(0,0)
        #self.Tail = self.Object(0,0)
        self.Map = dict({0:dict({0:self.Cell(1)})})
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0

    def make_move(self, direction, distance):
        print(f'{direction}, {distance}')
        i = 0
        while i < distance:
            self.MoveHead(direction)
            knotindex = 1
            while knotindex < len(self.Knots):
                self.MoveTail(knotindex)
                knotindex += 1
            self.Map[self.Knots[len(self.Knots)-1].x][self.Knots[len(self.Knots)-1].y].update_tailcount(1)
            i+=1
            pass

    def UpdateMap(self, x, y):
        if (x not in self.Map):
            self.Map[x] = dict({y:self.Cell(0)})
        elif (y not in self.Map[x]):
            self.Map[x][y] = self.Cell(0)
        else:
            cell = self.Map[x][y]
        if x < self.minx:
            self.minx = x
        if x > self.maxx:
            self.maxx = x
        if y < self.miny:
            self.miny = y
        if y > self.maxy:
            self.maxy = y

    def MoveHead(self, direction):
        if direction == 'U':
            self.Knots[0].y = self.Knots[0].y + 1
        if direction == "R":
            self.Knots[0].x = self.Knots[0].x + 1
        if direction == "L":
            self.Knots[0].x = self.Knots[0].x - 1
        if direction == 'D':
            self.Knots[0].y = self.Knots[0].y - 1
        self.UpdateMap(self.Knots[0].x,self.Knots[0].y)

    def MoveTail(self, i):
        if (abs(self.Knots[i-1].y - self.Knots[i].y) > 1) or (abs(self.Knots[i-1].x - self.Knots[i].x) > 1):
            if (self.Knots[i].y - self.Knots[i-1].y) != 0:
                if (self.Knots[i].y - self.Knots[i-1].y) > 0:
                    self.Knots[i].y = self.Knots[i].y - 1
                else:
                    self.Knots[i].y = self.Knots[i].y + 1
            if (self.Knots[i].x - self.Knots[i-1].x) != 0:
                if (self.Knots[i].x - self.Knots[i-1].x) > 0:
                    self.Knots[i].x = self.Knots[i].x - 1
                else:
                    self.Knots[i].x = self.Knots[i].x + 1
        self.UpdateMap(self.Knots[i].x,self.Knots[i].y)

    def PrintMap(self):
        y = self.maxy
        print('--------')
        while (y >= self.miny):
            row = ''
            x = self.minx
            while x <= self.maxx:
                cell_char = '.'
                if (y in self.Map[x]):
                    if self.Map[x][y].get_count_tail():
                        cell_char = 'X'
                if x == 0 and y == 0:
                    cell_char = 's'
                i = 1
                while i < len(self.Knots):
                    if (self.Knots[i].x == x) and (self.Knots[i].y == y):
                        cell_char = str(i)
                    i += 1
                if (self.Knots[0].x == x) and (self.Knots[0].y == y):
                    cell_char = "H"
                row = row + cell_char
                x += 1
            y -= 1
            print(f'{row}')
        print('--------')

    def count_locations(self):
        y = self.maxy
        count_tail = 0
        while (y >= self.miny):
            x = self.minx
            while x <= self.maxx:
                if (y in self.Map[x]):
                    if self.Map[x][y].get_count_tail():
                        count_tail += 1
                x += 1
            y -= 1
        print(f'Tail Locations: {count_tail}')


    class Cell():
        def __init__(self, initial_count = 0):
            self.count_tail = initial_count

        def update_tailcount(self, count_tail):
            if count_tail == 1:
                self.count_tail = 1

        def get_count_tail(self):
            return self.count_tail > 0

    class Object():
        def __init__(self, x, y):
            self.x = x
            self.y = y

class P91():
    def __init__(self, file):
        self.data = read_file(file)
        self.map = P91map(9)
        self.moves = []
        for r in self.data.split('\n'):
            move = r.split(' ')
            self.moves.append(dict({'direction': move[0],'distance': int(move[1])}))
        
    def run(self):
        for move in self.moves:
            self.map.make_move(move['direction'], move['distance'])
        self.map.PrintMap()
        self.map.count_locations()

class CPU():
    def __init__(self, commands):
        self.commands = commands
        self.registerx_history = []
        self.registerx = 1
        self.cycle = 0
        self.current_rowcycle = 0

    def update_cycle(self):
        if (self.current_rowcycle <= self.registerx + 1) and (self.current_rowcycle >= self.registerx - 1):
            print('#', end="")
        else:
            print('.', end="")
        self.registerx_history.append(self.registerx)
        self.cycle += 1
        if self.current_rowcycle == 39:
            self.current_rowcycle = 0
            print('')
        else:
            self.current_rowcycle += 1
        pass

    def process_command(self, command, value):
        if command == 'addx':
            self.update_cycle()
            self.update_cycle()
            self.registerx = self.registerx + value
        if command == 'noop':
            self.update_cycle()

    def get_signal_strength(self, cycle):
            return self.registerx_history[cycle-1] * cycle

    def run(self):
        for cmd in self.commands:
            if len(cmd) == 1:
                value = 0
            else:
                value = int(cmd[1])
            self.process_command(cmd[0], value)

    def print_commands(self):
        for cmd in self.commands:
            print(f'{cmd[0]}', end="")
            if len(cmd) > 1:
                print(f',{cmd[1]}')
            else:
                print("")


class P10_1():
    def __init__(self, file):
        self.data = read_file(file)
        self.commands = []
        for r in self.data.split('\n'):
            cmd = r.split(' ')
            self.commands.append(cmd)
        self.cpu = CPU(self.commands)


    def print_commands(self):
        self.cpu.print_commands()

    def run10_1(self):
        self.cpu.run()
        cycles = [20,60,100,140,180,220]
        signal_strengths = 0
        for c in cycles:
            signal_strengths = signal_strengths + self.cpu.get_signal_strength(c)
        print(f'{signal_strengths}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #row = problem71()
    #print(f'{row.sumDirectorcolSizes(100000)}')
    #row.findSmallestDirToDelete(70000000, 30000000)
    #row.testFilescolstem()
    #Problem81('8-1.input').isvisible()
    #Problem81('8-1.input').calculateMaxScenicScore()
    P10_1('10-1.input').run10_1()

