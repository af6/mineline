import sys,random
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
bac=[b,r,g,o,b,pu,c,lgra,dg,lr,lgre,y,lb,pi,lc]
ft="abcdefghijklmno"
size=int(sys.argv[1])
jump=1
world=list([[c]*size]*size)[::-1]
def build(x,y,b):
    global world
    world[y][x]=b
def save(world):
    i=open(sys.argv[2],"w")
    i.write(str([world,["Rock: 0","Diamond: 0","Wood: 0"]]))
    i.close()
def fill(s,x,y):
    xo=0
    yo=0
    s=s[::-1]
    for i in s.split("\n"):
        for a in i:
            xo+=1
            if a!=" ":
                world[y-yo][x+xo]=bac[ft.index(a)]
        yo+=1
        xo=0
save(world)
world=eval(open(sys.argv[2],"r").read())
world=world[0]
blocks=size**2
i=int((blocks)*(1/12))
i=0
j=0
a=0
gib=[]
count=0
prev=25
def go():
    global prev,world,count
    if count >= size:
        return None;
    if count == 0:
        world[24][0]=g
        gib.append(24)
    else:
        up=random.randint(0,1)
        if prev >= size-3:
            prev=size-3
        if up:
            world[prev+jump][count]=g
            prev+=jump
            gib.append(prev)
        else:
            world[prev-jump][count]=g
            prev-=jump
            gib.append(prev)
    count+=1
def go2():
    global prev,world,count
    if count >= size:
        return None;
    else:
        a=0
        while a<gib[count]-5:
            world[a][count]=dg
            a+=1
    count+=1
def go3():
    global prev,world,count
    i=random.randint(1,3)
    if i==1:
        fill("hhh\nhhh\nhhh\nccc\nccc\n c ",count,gib[count]+1)
    if count >= size:
        return None;
    else:
        a=gib[count]-5
        while a<gib[count]:
            world[a][count]=o
            a+=1
    count+=1
while a<size:
    go()
    a+=1
a=0
count=0
while a<size:
    go2()
    a+=1
a=0
count=0
while a<size:
    go3()
    a+=1
a=0
i=0
while i>0:
    a=i%3
    if a==0:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=dg
    if a==1:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=lb
    if a==2:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=lgra
    i-=1
save(world[::-1])
