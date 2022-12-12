import AoC_Shared

class Node():
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.indexed = False
        self.links = []
        self.distance = -1
    
    def add_links(self, map):
        coords = [[self.row-1,self.col],[self.row+1,self.col], [self.row, self.col-1], [self.row, self.col+1]]
        maxrows = len(map)
        maxcols = len(map[0])
        for c in coords:
            if (c[0] >= 0) and (c[0] < maxrows) and (c[1] >= 0) and (c[1] < maxcols):
                if ord(map[c[0]][c[1]].value) <= ord(self.value) + 1:
                    self.links.append(map[c[0]][c[1]])

    def check_distance(self, endnode, start = True):
        if self.indexed:
            return []
        if start == True:
            self.distance = 0
        links_to_check = []
        for l in self.links:
            if l.distance < 0:
                l.distance = self.distance + 1
            if l.distance > self.distance + 1:
                l.distance = self.distance + 1
            if l.indexed == False:
                links_to_check.append(l)
        self.indexed = True
        if self.row == endnode[0] and self.col == endnode[1]:
            return []
        else:
            return links_to_check

class Map():
    def __init__(self, maptext, part2=False):
        self.map = []
        y = 0
        for r in maptext.split('\n'):
            x = 0
            self.map.append([])
            for i in r:
                if i == 'S':
                    self.start = [y,x]
                    i = 'a'
                if i == 'E':
                    self.end = [y,x]
                    i = 'z'
                self.map[y].append(Node(i, y, x))
                x += 1
            y += 1
        self.index_nodes()
    
    def index_nodes(self):
        for r in self.map:
            for i in r:
                i.add_links(self.map)    
        startnode = self.map[self.start[0]][self.start[1]]
        links = startnode.check_distance(self.end, True)
        while len(links) > 0:
            link = links.pop(0)
            links_to_append = link.check_distance(self.end, False)
            if link.row == self.end[0] and link.col == self.end[1]:
                links = []
            else:
                for l in links_to_append:
                    links.append(l)
            #print(f'{len(links)}')

    def printmap(self):
        for r in self.map:
            for i in r:
                print(f'{i.value}', end="")
            print("")
    
    def print_numlinks(self):
        for r in self.map:
            for i in r:
                print(f'{len(i.links)}', end="")
            print("")

    def print_distance(self):
        for r in self.map:
            for i in r:
                txt = "{:4d}"
                #print(txt.format(i.distance), end="")
            #print("")
        print(f'Distance to end: {str(self.map[self.end[0]][self.end[1]].distance)}')

    def test(self):
        self.printmap()
        x = self.map[1][3]
        x.value = '@'
        print("")
        self.printmap()
        print("")
        self.print_numlinks()


def Run():
    map = Map(AoC_Shared.read_file('12-1.input'))
    #map.test()
    map.print_distance()

if __name__ == '__main__':
    Run()

