import functools
import AoC_Shared

class Area():
    def __init__(self, rock_lines, add_floor = False) -> None:
        self.floor = add_floor
        self.sand = 0
        minx = 500
        maxx = 500
        miny = 0
        maxy = 0
        self.area = []
        for line in rock_lines:
            for rock in line:
                minx = min(rock[0], minx)
                maxx = max(rock[0], maxx)
                miny = min(rock[1], miny)
                maxy = max(rock[1], maxy)
        if add_floor:
            maxy = maxy + 2
            rock_lines.append([[minx,maxy],[maxx,maxy]])
        self.maxy = maxy
        self.maxx = maxx
        self.minx = minx
        for i in range (miny,maxy+1):
            c = []
            for j in range(minx,maxx+1):
                c.append('.')
            self.area.append(c)
        for line in rock_lines:
            i = 1
            while i < len(line):
                rock_1 = line[i-1]
                rock_2 = line[i]
                x_start = min(rock_1[0], rock_2[0])
                x_end = max(rock_1[0], rock_2[0])
                y_start = min(rock_1[1], rock_2[1])
                y_end = max(rock_1[1], rock_2[1])
                for y in range(y_start, y_end+1):
                    for x in range(x_start, x_end+1):
                        self.area[y-miny][x-minx] = '#'
                i += 1
    
    def insert_x(self, floor = False):
        if floor:
            i = 0
            for y in self.area:
                if i == self.maxy:
                    y.insert(0,'#')
                else:
                    y.insert(0,'.')
                i += 1
            self.minx = self.minx - 1

    def append_x(self, floor = False):
        if floor:
            i = 0
            for y in self.area:
                if i == self.maxy:
                    y.append('#')
                else:
                    y.append('.')
                i += 1
            self.maxx = self.maxx + 1

    def print_area(self):
        for x in self.area:
            for y in x:
                print(f'{y}', end="")
            print("")

    def drop_sand(self):
        floor = self.floor
        x = 500
        y = 0
        if self.area[y][x-self.minx] == 'o':
            return False
        while True:
            if (y + 1) > self.maxy:
                return False
            if self.area[y+1][x-self.minx] == '.':
                y += 1
                if x + 1 > self.maxx:
                    self.append_x(floor)
                if x - 1 < self.minx:
                    self.insert_x(floor)
                    return floor
            elif self.area[y+1][x-1-self.minx] == '.':
                y += 1
                x -= 1
                if x - 1 < self.minx:
                    self.insert_x(floor)
                if x + 1 > self.maxx:
                    return False
            elif self.area[y+1][x+1-self.minx] == '.':
                y += 1
                x += 1
                if x + 1 > self.maxx:
                    self.append_x(floor)
            else:
                self.area[y][x-self.minx] = 'o'
                self.sand = self.sand + 1
                return True





def Run():
    rock_lines = [[[int(x) for x in rock.split(',')] for rock in line.split(' -> ')] for line in AoC_Shared.read_file('p14.input').split('\n')]
    map_part1 = Area(rock_lines)
    while map_part1.drop_sand():
        pass
    print(f'Part 1: {map_part1.sand}')
    #map_part1.print_area()
    map_part2 = Area(rock_lines, True)
    while map_part2.drop_sand():
        pass
    print(f'Part 2: {map_part2.sand}')
    #map_part2.print_area()


if __name__ == '__main__':
    Run()
