import functools
import AoC_Shared
import re

## Brute force approach...
class Area():
    def beacon_distance(self, sensor):
        return (abs(sensor['beacon']['x'] - sensor['sensor']['x']) + abs(sensor['beacon']['y'] - sensor['sensor']['y']))
    
    def __init__(self, sensors) -> None:
        minx = 999
        maxx = -999
        miny = 999
        maxy = -999
        self.area = []
        for sensor in sensors:
            minx = min(sensor['sensor']['x'] - self.beacon_distance(sensor),minx)
            maxx = max(sensor['sensor']['x'] + self.beacon_distance(sensor),maxx)
            miny = min(sensor['sensor']['y'] - self.beacon_distance(sensor), miny)
            maxy = max(sensor['sensor']['y'] + self.beacon_distance(sensor), maxy)
        self.maxy = maxy
        self.maxx = maxx
        self.minx = minx
        self.miny = miny
        for i in range (miny,maxy+1):
            c = []
            for j in range(minx,maxx+1):
                c.append('.')
            self.area.append(c)
        i = 0
        for sensor in sensors:
            self.area[sensor['sensor']['y']-miny][sensor['sensor']['x']-minx] = 's'
            self.area[sensor['beacon']['y']-miny][sensor['beacon']['x']-minx] = 'b'
            b_dist = self.beacon_distance(sensor)
            j = 0
            for y in range(sensor['sensor']['y'] - b_dist, sensor['sensor']['y'] + b_dist + 1):
                j += 1
                x_range = b_dist - abs(y - sensor['sensor']['y'])
                for x in range(sensor['sensor']['x'] - x_range, sensor['sensor']['x'] + x_range + 1):
                    if self.area[y-miny][x-minx] == '.':
                        self.area[y-miny][x-minx] = '#'
                print(f'{i}, {j}', end='\r')
            i += 1
            pass

    def print_area(self):
        for x in self.area:
            for y in x:
                print(f'{y}', end="")
            print("")

    def check_row(self, row):
        count = 0
        for c in self.area[row-self.miny]:
            if c != '.' and c != 'b':
                count = count + 1
        return count



class Area_2():
    def beacon_distance(self, sensor):
        return (abs(sensor['beacon']['x'] - sensor['sensor']['x']) + abs(sensor['beacon']['y'] - sensor['sensor']['y']))
    
    def __init__(self, sensors) -> None:
        self.sensors = sensors
        minx = maxx = sensors[0]['sensor']['x']
        miny = maxy = sensors[0]['sensor']['y']
        for sensor in sensors:
            minx = min(sensor['sensor']['x'] - self.beacon_distance(sensor),minx)
            maxx = max(sensor['sensor']['x'] + self.beacon_distance(sensor),maxx)
            miny = min(sensor['sensor']['y']- self.beacon_distance(sensor), miny)
            maxy = max(sensor['sensor']['y']+ self.beacon_distance(sensor), maxy)
        self.maxy = maxy
        self.maxx = maxx
        self.minx = minx
        self.miny = miny

    def check_row(self, y):
        count = 0
        for x in range(self.minx, self.maxx + 1):
            no_beacon = False
            for sensor in self.sensors:
                if sensor['sensor']['x'] == x and sensor['sensor']['y'] == y:
                    no_beacon = True
                    break
                if sensor['beacon']['x'] == x and sensor['beacon']['y'] == y:
                    no_beacon = False
                    break
                if abs(sensor['sensor']['x'] - x) + abs(sensor['sensor']['y'] - y) <= self.beacon_distance(sensor):
                    no_beacon = True
            if no_beacon: count += 1
        return count

def Run():
    
    rows = [row for row in AoC_Shared.read_file('p15.input').split('\n')]
    sensors = []
    for row in rows:
        #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        m = re.match(r'Sensor at x=(?P<sensor_x>.*), y=(?P<sensor_y>.*): closest beacon is at x=(?P<beacon_x>.*), y=(?P<beacon_y>.*)',row)
        sensors.append({'sensor': {'x': int(m.group('sensor_x')), 'y': int(m.group('sensor_y'))}, 'beacon': {'x': int(m.group('beacon_x')), 'y': int(m.group('beacon_y'))}})
    map = Area_2(sensors)
    #map.print_area()
    print (f'Part 1: {map.check_row(2000000)}')

if __name__ == '__main__':
    Run()
