import math
import AoC_Shared


class PastMoves():
    def __init__(self) -> None:
        self.pastmoves = []

    def insertmove(self,move):
        self.pastmoves.append(move)
        #print(f'{move}')

moves = PastMoves()

class Monkey():

    def __init__(self, input) :
        rows = input.split('\n')
        items_str = rows[1].split(': ')
        self.items = []
        for i in items_str[1].split(','):
            self.items.append(int(i))
        ops_str = rows[2].split(': ')[1].split(' ')
        self.operator = ops_str[3]
        if ops_str[4] == 'old':
            self.operationval = -1
        else:
            self.operationval = int(ops_str[4])
        self.testval = int(rows[3].split(': ')[1].split(' ')[2])
        self.truemonkey = int(rows[4].split(': ')[1].split(' ')[3])
        self.falsemonkey = int(rows[5].split(': ')[1].split(' ')[3])
        self.inspected_items = 0
        self.lcm = 0
       
    def setlcm(self, value):
        self.lcm = value

    def getoperator(self):
        return self.operator

    def operation(self, value):
        if self.operationval < 0:
            op_val = value
        else:
            op_val = self.operationval
#        if value % self.lcm == 0:
#            if self.operator == '+':
#                return op_val
#            if self.operator == '*':
#                return self.lcm
#        else:
        if self.operator == '+':
            returnval = value + op_val
        if self.operator == '*':
            returnval = value * op_val
        if returnval % self.lcm == 0:
            return self.lcm
        else:
            return returnval % self.lcm
    
    def test(self, value):
        if value % self.testval == 0:
            return self.truemonkey
        else:
            return self.falsemonkey

    def inspectitem(self, monkeys):
        if len(self.items) == 0:
            return False
        item = self.items.pop(0)
        item = self.operation(item)
#       item = item / 3
        #item = math.trunc(item)
        monkeys[self.test(item)].throw(item)
        self.inspected_items += 1
        #moves.insertmove(self.test(item))
        return (len(self.items) > 0)
    
    def throw(self, value):
        self.items.append(value)

def get_common_factor(monkeys):
    lcm = 1
    for m in monkeys:
        lcm = lcm * m.testval
    return lcm




def Run():
    Monkeys = []
    monkey_strings = AoC_Shared.read_file('11-1.input').split('\n\n')
    #monkey_strings = AoC_Shared.read_file('11-1-test.input').split('\n\n')
    for m in monkey_strings:
        Monkeys.append(Monkey(m))
    
    for m in Monkeys:
        m.setlcm(get_common_factor(Monkeys))
    i = 0
    while i < 10000:
        for m in Monkeys:
            while (m.inspectitem(Monkeys) == True):
                pass
        print(f'{i}',end="\r")
        i += 1
    print("\n")
    inspected_items = []
    for m in Monkeys:
        inspected_items.append(m.inspected_items)
    for i in inspected_items:
        print(f'{i}')
    inspected_items.sort(reverse=True)
    print(f'{inspected_items[0]*inspected_items[1]}')

if __name__ == '__main__':
    Run()

