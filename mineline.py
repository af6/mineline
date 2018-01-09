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
rock=dg
wood=lgra
world=[[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock],[rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock,rock]][::-1]
sb="wood"
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
def Player():
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
            build(x,y,eval(sb))
def start():
    global world,x,y,world
    x=10+random.randint(0,len(world)-11)
    y=random.randint(0,len(world)-1)
    Thread(target=Player).start()
    while True:
        os.system("clear")
        print_world()
        time.sleep(.05)
start()
