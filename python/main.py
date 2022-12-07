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


class Filsystem():
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
        self.fs = Filsystem()
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
    
    def sumDirectorySizes(self, maxsize):
        return self.directorySizes(maxsize, self.fs.tree)

    def directorySizes(self, maxsize, folder):
        count = 0
        size = folder.getFolderSizeRecursive()
        if size <= maxsize:
            count += size
        for f in folder.getFolders().values():
            count += self.directorySizes(maxsize, f)
        return count
    
    def findDirectoryToFreeUpSpace (self, minimum, folder):
        size = folder.getFolderSizeRecursive()
        folders = []
        if size >= minimum:
            for f in folder.getFolders().values():
                if self.findDirectoryToFreeUpSpace(minimum, f) != 0:
                    folders.append(self.findDirectoryToFreeUpSpace(minimum, f))
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
        folder = self.findDirectoryToFreeUpSpace(amount_to_free_up, self.fs.tree)
        print(f'{folder.getFolderSizeRecursive()}')

    def testFilesystem(self):
        fs = Filsystem()
        fs.changeDir('/')
        fs.addFile('abc', 123)
        fs.addFile('def', 1234)
        fs.addDir('test1')
        fs.addDir('test2')
        fs.changeDir('test2')
        fs.addFile('xyz', 111)
        fs.addFile('aaa', 22222)
        #print(f'{fs.tree["/"]}')
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = problem71()
    print(f'{x.sumDirectorySizes(100000)}')
    x.findSmallestDirToDelete(70000000, 30000000)
    #x.testFilesystem()

