import functools
import AoC_Shared

#No longer needed since Parse_Into_List is deprecated
def GetListChunk(str):
    loop = True
    i = 1
    left = 1
    right = 0
    while loop:
        if str[i] == '[':
            left += 1
        if str[i] == ']':
            right += 1
        if left == right:
            return i
        i += 1

#This function has a subtle bug... and was useless once I discovered the eval() function.
def Parse_Into_List(str):
    vals = []
    loop = True
    while loop:
        if str[0] == '[':
            split_index = GetListChunk(str)
            chunk = str[1:][:split_index-1]
            remaining = str[split_index+1:]
            if chunk != '':
                vals.append(Parse_Into_List(chunk))
            if len(remaining) > 0:
                if remaining[0] == ',':
                    str = remaining[1:]
                else:
                    raise Exception("Invalid character")
            else:
                return vals
        else:
            str_split = str.split(',',1)
            vals.append(int(str_split[0]))
            if len(str_split) > 1:
                str = str_split[1]
            else:
                loop = False
                return vals

#This function has a subtle bug that I haven't figured out...
def Test_Pair(x, y):
    if isinstance(x, int) and isinstance(y,int):
        return x - y
    else:
        if isinstance(x, int):
            x = [x]
        if isinstance(y, int):
            y = [y]
        i = 0
        if len(x) != len(y):
            if len(x) == 0:
                return -1
            if len(y) == 0:
                return 1
        for val in x:
            if len(y) == 0:
                return 1
            y_val = y.pop(0)
            tp_val = Test_Pair(val, y_val)
            if tp_val != 0:
                return tp_val
        if len(x) == len(y):
            return 0
        else:
            return -1

#Stole this from reddit... not sure why this one works but mine doesn't.
def compare(lh, rh):
    if lh == []:
        return 0 if rh == [] else -1
    if rh == []:
        return 1
    if isinstance (lh, list):
        if isinstance (rh, list):
            cmp = compare(lh[0], rh[0])
            if cmp == 0:
                return compare(lh[1:], rh[1:])
            return cmp
        return compare(lh, [rh])
    if isinstance (rh, list):
        return compare([lh], rh)
    return -1 if lh < rh else 1 if rh < lh else 0

def Run():
    pairs = [[eval(s) for s in pair.split('\n')] for pair in AoC_Shared.read_file('13-1.input').split('\n\n')]
    i = 1
    sum = 0
    pairlist = []
    for pair in pairs:
        #split_pair = pair.split('\n')
        #These functions didn't work, and couldn't figure out why.
        #val = Test_Pair(Parse_Into_List(split_pair[0]),Parse_Into_List(split_pair[1]))
        #val = Test_Pair(eval(split_pair[0]),eval(split_pair[1]))
        ###

        val = compare(pair[0],pair[1])
        if val < 0:
            sum = sum + i
        i += 1
        pairlist.append(pair[0])
        pairlist.append(pair[1])
    print(f'Part 1: {sum}')
    i = 0
    pairlist.append([[2]])
    pairlist.append([[6]])
    while i < len(pairlist) - 1:
        j = i + 1
        while j < len(pairlist):
            if compare(pairlist[i], pairlist[j]) > 0:
                swap = pairlist[i]
                pairlist[i] = pairlist[j]
                pairlist[j] = swap
            j = j + 1
        i = i + 1
    vals = []
    i = 1
    for pair in pairlist:
        if compare(pair, [[2]]) == 0 or compare(pair, [[6]]) == 0:
            vals.append(i)
        i += 1
    print(f'Part 2: {vals[0]*vals[1]}')


if __name__ == '__main__':
    Run()
