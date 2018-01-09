import os,time,sys,random
import threading
from threading import Thread
bla="\033[39m"
b='\033[30m'
r='\033[31m'
g='\033[32m'
o='\033[33m'
b='\033[34m'
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
blocks=[b,r,g,o,pu,c,lgra,dg,lr,lgre,y,lb,pi,lc]
bn=["coal","melon","grass","oranges","grapefruit","water","wood","rock","settle","turf","lemon","diamond","ruby","polished diamond"]
print(len(blocks))
rock=dg
wood=lgra
sb=bn[6]
cbn=blocks[6]
def print(value):
    sys.stdout.write(value+"\n")
def getChar(): # StackOverFlow: https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
    # figure out which function to use once, and store it in _func
    if "_func" not in getChar.__dict__:
        try:
            # for Windows-based systems
            import msvcrt # If successful, we are on Windows
            getChar._func=msvcrt.getch

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
def print_world():
    global b
    a=0
    itmp=[]
    for i in world:
        itmp=list(i)
        if y==a:
            itmp[x]=b
        print('█'.join(itmp))
        a+=1
    print("\n\n\n"+sb)
    if invTime<time.time()+10:
        print("Inventory:\n\n"+"\n\n".join(Inventory))
    print(bla)
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
    i=open(sys.argv[1],"w")
    i.write(str([world,Inventory]))
    i.close()
def load():
    global world,Inventory
    i=open(sys.argv[1],"r")
    i2=i.read()
    world=eval(i2)[0]
    Inventory=eval(i2)[1]
    i.close()
def Player():
    global cbn,sb,Inventory,invTime
    invTime=2000000000
    while True:
        char=getChar()
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
            if sb=="rock":
                abcd=0
                abcd2=5
            elif sb=="diamond":
                abcd=1
                abcd2=9
            elif sb=="wood":
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
                print("diamond")
                Inventory[1]=str("Diamond: ")+str(int(Inventory[1][9:])+1)
            if world[y][x]==lgra:
                Inventory[2]=str("Wood: ")+str(int(Inventory[2][5:])+1)            
            build(x,y,g)
        if char=="c":
            try:
                sb=bn[bn.index(sb)-1]
                cbn=blocks[blocks.index(cbn)-1]
            except:
                sb=bn[14]
                cbn=blocks[14]
        if char=="v":
            try:
                sb=bn[bn.index(sb)+1]
                cbn=blocks[blocks.index(cbn)+1]
            except:
                sb=bn[0]
                cbn=blocks[0]
        if char=="i":
            invTime=time.time()
def start():
    load()
    global world,x,y,world
    x=10+random.randint(0,len(world)-11)
    y=random.randint(0,len(world)-1)
    Thread(target=Player).start()
    avg_fps=0
    frames=0
    while True:
        os.system("clear")
        bef = time.time()
        print_world()
        frames+=1
        aft = time.time()
        avg_fps*=frames-1
        avg_fps+=aft-bef
        avg_fps/=frames
        print(str(int(1/avg_fps))+" FPS")
        abc=random.randint(5,20)
        time.sleep(1/abc)
start()
