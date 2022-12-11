import AoC_Shared

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
       

    def operation(self, value):
        if self.operationval < 0:
            op_val = value
        else:
            op_val = self.operationval
        if self.operator == '+':
            return value + op_val
        if self.operator == '*':
            return value * op_val
        raise Exception("Invalid operator")
    
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
        item = item / 3
        item = int(item)
        monkeys[self.test(item)].throw(item)
        self.inspected_items += 1
        return (len(self.items) > 0)
    
    def throw(self, value):
        self.items.append(value)


if __name__ == '__main__':
    Monkeys = []
    monkey_strings = AoC_Shared.read_file('11-1.input').split('\n\n')
#    monkey_strings = AoC_Shared.read_file('11-1-test.input').split('\n\n')
    for m in monkey_strings:
        Monkeys.append(Monkey(m))
    i = 0
    while i < 20:
        for m in Monkeys:
            while (m.inspectitem(Monkeys) == True):
                pass
        i += 1
    inspected_items = []
    for m in Monkeys:
        inspected_items.append(m.inspected_items)
    inspected_items.sort(reverse=True)
    print(f'{inspected_items[0]*inspected_items[1]}')

