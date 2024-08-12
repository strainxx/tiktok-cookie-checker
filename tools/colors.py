from tools.smath import clamp

def invert_color(col):
    inv = []
    for c in col:
        inv.append(255-c)
    return inv

def fix_color(col):
    res = []
    for i in col:
        if i > 255:
            res.append(0)
            continue
        if i < 0:
            res.append(255)
            continue
        res.append(i)
    # print("FROM:", col, "TO", res)
    return res