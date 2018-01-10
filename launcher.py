import os,sys,time
os.system("clear")
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
def new(file,size):
    print("Generating...")
    code=-1
    while code!=0:
        code=os.system("python3 "+"/".join(sys.argv[0].split("/")[:-1])+"/genWorld.py "+str(size)+" "+file)
    load(file)
def load(file):
    os.system("clear;python3 "+"/".join(sys.argv[0].split("/")[:-1])+"/mineline.py "+file)
def go():
    print("""
___  ____            _     _            
|  \/  (_)          | |   (_)           
| .  . |_ _ __   ___| |    _ _ __   ___ 
| |\/| | | '_ \ / _ \ |   | | '_ \ / _ \\
| |  | | | | | |  __/ |___| | | | |  __/
\_|  |_/_|_| |_|\___\_____/_|_| |_|\___|
                                       """)
    print("""
A ) Load File
B ) New File
C ) Exit""")
    c=getChar()
    if c=="a":
        file=input("File: ")
        load(file)
    elif c=="b":
        file=input("file: ")
        size=int(input("size: "))
        new(file,size)
    elif c=="c":
        return 0;
go()
