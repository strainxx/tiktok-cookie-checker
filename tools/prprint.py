from tools import colors

rn = [254, 0, 0]

rk = -3
gk = 0
bk = 3

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def rnprint(*a, prefix: str = ">>>"):
    global rn, rk, gk, bk
    omg = " ".join(map(str, a))
    # print(rn)
    print(get_color_escape(*colors.invert_color(rn)) 
      + get_color_escape(*rn, background=True)
      + prefix
      + RESET, omg)
    rn = [rn[0]+rk, rn[1]+gk, rn[2]+bk]
    # print
    if rn[0] == 0:
        rk = -rk
    if rn[1] == 0:
        gk = -gk
    if rn[2] == 0:
        gk = -bk
      
    if rn[0] == 255:
        rk = -rk
    if rn[1] == 255:
        gk = -gk
    if rn[2] == 255:
        gk = -bk
    rn = colors.fix_color(rn)