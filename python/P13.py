import AoC_Shared

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

def Test_Pair(x, y):
    if isinstance(x, int) and isinstance(y,int):
        return x - y
    else:
        if isinstance(x, int):
            x = [x]
        if isinstance(y, int):
            y = [y]
        i = 0
        for val in x:
            if len(y) <= i:
                return 1
            if Test_Pair(val, y[i]) != 0:
                return Test_Pair(val, y[i])
            i += 1
        if len(x) == len(y):
            return 0
        else:
            return -1

def Run():
    pairs = AoC_Shared.read_file('13-1.test').split('\n\n')
    i = 1
    sum = 0
    for pair in pairs:
        split_pair = pair.split('\n')
        val = Test_Pair(Parse_Into_List(split_pair[0]),Parse_Into_List(split_pair[1]))
        if val < 0:
            sum = sum + i
            print(i)
        i += 1
    print(sum)
if __name__ == '__main__':
    Run()
    #index = GetListChunk('[[1,5,[0,3],[20,10],8],6]')
    #vals = Parse_Into_List('[[1,5,[0,3],[20,10],8],6]')
    print(list)


