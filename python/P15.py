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
    def __init__(self, sensors) -> None:
        self.sensors = sensors
        minx = maxx = self.minx_sensor = self.maxx_sensor = sensors[0]['sensor']['x']
        miny = maxy = self.miny_sensor = self.maxy_sensor = sensors[0]['sensor']['y']
        for sensor in sensors:
            minx = min(sensor['sensor']['x'] - self.beacon_distance(sensor),minx)
            maxx = max(sensor['sensor']['x'] + self.beacon_distance(sensor),maxx)
            miny = min(sensor['sensor']['y']- self.beacon_distance(sensor), miny)
            maxy = max(sensor['sensor']['y']+ self.beacon_distance(sensor), maxy)
            self.minx_sensor = min(sensor['sensor']['x'],self.minx_sensor)
            self.maxx_sensor = max(sensor['sensor']['x'],self.maxx_sensor)
            self.miny_sensor = min(sensor['sensor']['y'],self.miny_sensor)
            self.maxy_sensor = max(sensor['sensor']['y'],self.maxy_sensor)
        self.maxy = maxy
        self.maxx = maxx
        self.minx = minx
        self.miny = miny

    def beacon_distance(self, sensor):
        return (abs(sensor['beacon']['x'] - sensor['sensor']['x']) + abs(sensor['beacon']['y'] - sensor['sensor']['y']))

    def sensor_proximity(self, sensor, x, y):
        beacon_dist = self.beacon_distance(sensor)
        sensor_dist = abs(sensor['sensor']['x'] - x) + abs(sensor['sensor']['y'] - y)
        return sensor_dist, beacon_dist

    def find_beacon_sensor(self, sensor):
        r = self.beacon_distance(sensor) + 1
        increment = -1
        x = sensor['sensor']['x']
        y = sensor['sensor']['y'] + r
        x_origin = x
        y_origin = y
        while True:
            loopbreak = False
            if x > self.maxx_sensor or x < self.minx_sensor or y > self.maxy_sensor or y < self.miny_sensor:
                loopbreak = True
            else:
                beacon_dist = []
                sensor_dist = []
                for s in self.sensors:
                    if s != sensor:
                        sensor_dist_v, beacon_dist_v = self.sensor_proximity(s,x,y)
                        sensor_dist.append(sensor_dist_v)
                        beacon_dist.append(beacon_dist_v)
                        if sensor_dist_v <= beacon_dist_v: #if there is sensor overlap, then this isn't the spot - move on
                            loopbreak = True
                            break
            if not loopbreak:
                return x * 4000000 + y # if made it through all sensors
            y += increment
            if increment < 0:
                x = sensor['sensor']['x'] - (abs(sensor['sensor']['y'] - y) - r)
            else:
                x = sensor['sensor']['x'] + (abs(sensor['sensor']['y'] - y) - r)
            if abs(sensor['sensor']['y'] - y) == r:
                increment = increment * -1
            if (abs(x - sensor['sensor']['x']) + abs(y - sensor['sensor']['y'])) != r:
                raise Exception("r doesn't match!")
            if x == x_origin and y == y_origin:
                return -1

    def find_beacon(self):
        i = 1
        for sensor in self.sensors:
            print(f'Sensor {i} out of {len(self.sensors)}', end='\r')
            i += 1
            found = self.find_beacon_sensor(sensor)
            if found > 0:
                print("")
                return found
        return found
    
    def check_row(self, y):
        count = 0
        for x in range(self.minx, self.maxx + 1):
            val = self.check_beacon(x,y)
            if val == '#' or val == 's':
                count += 1
        return count

    def find_beacon_old(self):
        ymin = xmin = 0
        ymax = xmax = 4000000
        ymin = max(self.miny, 0)
        xmin = max(self.minx, 0)
        ymax = min(self.maxy_sensor, 4000000)
        xmax = min(self.maxx_sensor, 4000000)
        for y in range(ymin, ymax):
            for x in range(xmin, xmax):
                if self.check_beacon(x,y) == '.':
                    return x * 4000000 + y
                

    def check_beacon(self, x, y):
        no_beacon = False
        for sensor in self.sensors:
            if sensor['sensor']['x'] == x and sensor['sensor']['y'] == y:
                no_beacon = True
                return 's'
            if sensor['beacon']['x'] == x and sensor['beacon']['y'] == y:
                no_beacon = False
                return 'b'
            if abs(sensor['sensor']['x'] - x) + abs(sensor['sensor']['y'] - y) <= self.beacon_distance(sensor):
                no_beacon = True
        if no_beacon == True:
            return '#'
        else:
            return '.'
    
def Run():
    rows = [row for row in AoC_Shared.read_file('p15.input').split('\n')]
    sensors = []
    for row in rows:
        #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        m = re.match(r'Sensor at x=(?P<sensor_x>.*), y=(?P<sensor_y>.*): closest beacon is at x=(?P<beacon_x>.*), y=(?P<beacon_y>.*)',row)
        sensors.append({'sensor': {'x': int(m.group('sensor_x')), 'y': int(m.group('sensor_y'))}, 'beacon': {'x': int(m.group('beacon_x')), 'y': int(m.group('beacon_y'))}})
    map = Area_2(sensors)
    #map.print_area()
    #print (f'Part 1: {map.check_row(2000000)}')
    #print (f'Part 1 test: {map.check_row(10)}')
    print (f'Part 2: {map.find_beacon()}')

if __name__ == '__main__':
    Run()
