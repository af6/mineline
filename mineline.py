import os,time,sys,random
import threading
from threading import Thread
jump=1
i=0
j=0
a=0
gib=[]
count=0
prev=25
bla2="\033[39m"
bla='\033[30m'
r='\033[31m'
g='\033[32m'
o='\033[33m'
br='\033[0;33;47m'
blu='\033[34m'
pu='\033[35m'
c='\033[36m'
lgra='\033[37m'
dg='\033[90m'
lr='\033[91m'
lgre='\033[92m'
y='\033[93m'
lb='\033[94m'
pi='\033[95m'
lc='\033[96m'
blocks=[bla,r,g,blu,pu,c,lgra,dg,lr,lgre,y,lb,pi,lc]
bn=["Coal","Melon","Grass","Oranges","Water","Grapefruit","Pond","Wood","Rock","Settle","Turf","Lemon","Diamond","Ruby","Polished Diamond"]
file=sys.argv[1]
rock=dg
wood=lgra
sb=bn[6]
cbn=blocks[6]
def getChar(): # StackOverFlow: https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
    # figure out which function to use once, and store it in _func
    if "_func" not in getChar.__dict__:
        try:
            # for Windows-based systems
            import msvcrt # If successful, we are on Windows
            getChar._func=msvcrt.getch
            print("win")
        except ImportError:
            # for POSIX-based systems (with termios & tty support)
            import tty, sys, termios # raises ImportError if unsupported

            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)

                try:
                    tty.setcbreak(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

                return answer

            getChar._func=_ttyRead
    return getChar._func()
def Render():
    global b,itmp,lp,avg_fps
    itmp=eval(str(world[y-16:y+16]))
    itmp[15][x]=blu
    for i in itmp:
        sys.stdout.write("█".join(i[x-16:x+16])+"\n")
    itmp2="./render"
    a=0
    try:
        if invTime<time.time()+10:
            sys.stdout.write("Inventory:\n\n"+"\n\n".join(Inventory)+"\n")
    except:
        pass
    clear()
def build(x,y,b):
    global world
    world[y][x]=b
def up():
    global y
    y-=1
def left():
    global x
    x-=1
def down():
    global y
    y+=1
def right():
    global x
    x+=1
def save(world):
    i=open(file,"w")
    i.write(str([world,Inventory]))
    i.close()
def load():
    global world,Inventory,frames,x,y,FLY
    try:
        FLY
    except:
        FLY=False
    i=open(file,"r")
    i2=i.read()
    world=eval(i2)[0]
    Inventory=eval(i2)[1]
    i.close()
def Player():
    try:
        global cbn,sb,Inventory,invTime,x,y
        x=128
        y=230
        invTime=2000000000
        while True:
            char=getChar()
            if sys.platform=="win32":
                if char==b"w":
                    up()
                if char==b"a":
                    left()
                if char==b"s":
                    down()
                if char==b"d":
                    right()
                if char==b"b":
                    abcd=0
                    abcd2=0
                    if sb=="Rock":
                        abcd=0
                        abcd2=5
                    elif sb=="Diamond":
                        abcd=1
                        abcd2=9
                    elif sb=="Wood":
                        abcd=2
                        abcd2=5
                    if int(Inventory[abcd][abcd2:])>0:
                        Inventory[abcd]=str(["Rock: ","Diamond: ","Wood: "][abcd])+str(int(Inventory[abcd][abcd2:])-1)
                        build(x,y,cbn)
                if char==b"x":
                    save(world)
                if char==b"r":
                    if world[y][x]==dg:
                        Inventory[0]=str("Rock: ")+str(int(Inventory[0][5:])+1)
                    if world[y][x]==lb:
                        Inventory[1]=str("Diamond: ")+str(int(Inventory[1][9:])+1)
                    if world[y][x]==lgra:
                        Inventory[2]=str("Wood: ")+str(int(Inventory[2][5:])+1)            
                    build(x,y,c)
                if char==b"c":
                    try:
                        sb=bn[bn.index(sb)-1]
                        cbn=blocks[blocks.index(cbn)-1]
                    except:
                        sb=bn[15]
                        cbn=blocks[15]
                if char==b"v":
                    try:
                        sb=bn[bn.index(sb)+1]
                        cbn=blocks[blocks.index(cbn)+1]
                    except:
                        sb=bn[0]
                        cbn=blocks[0]
                if char==b"i":
                    invTime=time.time()
            else:
                if char=="w":
                    up()
                if char=="a":
                    left()
                if char=="s":
                    down()
                if char=="d":
                    right()
                if char=="b":
                    abcd=0
                    abcd2=0
                    if sb=="Rock":
                        abcd=0
                        abcd2=5
                    elif sb=="Diamond":
                        abcd=1
                        abcd2=9
                    elif sb=="Wood":
                        abcd=2
                        abcd2=5
                    if int(Inventory[abcd][abcd2:])>0:
                        Inventory[abcd]=str(["Rock: ","Diamond: ","Wood: "][abcd])+str(int(Inventory[abcd][abcd2:])-1)
                        build(x,y,cbn)
                if char=="x":
                    save(world)
                if char=="r":
                    if world[y][x]==dg:
                        Inventory[0]=str("Rock: ")+str(int(Inventory[0][5:])+1)
                    if world[y][x]==lb:
                        Inventory[1]=str("Diamond: ")+str(int(Inventory[1][9:])+1)
                    if world[y][x]==lgra:
                        Inventory[2]=str("Wood: ")+str(int(Inventory[2][5:])+1)            
                    build(x,y,c)
                if char=="c":
                    clear()
                    try:
                        sb=bn[bn.index(sb)-1]
                        cbn=blocks[blocks.index(cbn)-1]
                    except:
                        sb=bn[15]
                        cbn=blocks[15]
                if char=="v":
                    clear()
                    try:
                        sb=bn[bn.index(sb)+1]
                        cbn=blocks[blocks.index(cbn)+1]
                    except:
                        sb=bn[0]
                        cbn=blocks[0]
                if char=="i":
                    invTime=time.time()
    except:
        sys.stdout.write("""
 ________________________
|Mineline has crashed.   |
|We apologize for the    |
|Inconveinence.          |
\________________________/""")
def clear():
    sys.stdout.write("\n\n\n\n\n\n\r\r\r\r\r\r"+"\x1b[A"*1024)
def start():
    global world,x,y,world,file,Inventory,avg_fps,lp
    avg_fps=0
    frames=0
    done=0
    lp=0
    try:
        if DEV_MODE:
            Inventory=["Rock: 999999999","Diamond: 999999999","Wood: 999999999"]
    except:
        pass
    avg_fps=0.1
    frames=0
    file=sys.argv[1]
    load()
    Thread(target=Player).start()
    x=17
    y=len(world)-(26+1)
    while True:
        bef = time.time()
        Render()
        sys.stdout.write("\x1b[A"*len(sb)+"\n")
        frames+=1
        aft = time.time()
        avg_fps*=frames-1
        avg_fps+=aft-bef
        avg_fps/=frames
        try:
            if world[y+1][x]==c and not FLY:
                y=y+1
            if world[y+1][x]!=g and not world[y+1][x]==c:
                y=y-1
        except:
            pass
start()
