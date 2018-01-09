import sys,random
g='\033[32m'
dg='\033[90m'
lb='\033[94m'
lgra='\033[37m'
size=int(sys.argv[1])
world=list([[g]*size]*size)
def save(world):
    i=open(sys.argv[2],"w")
    i.write(str([world,["Rock: 0","Diamond: 0","Wood: 0"]]))
    i.close()
save(world)
world=eval(open(sys.argv[2],"r").read())
world=world[0]
i=50
while i>0:
    a=i%3
    if a==0:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=dg
    if a==1:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=lb
    if a==2:
        world[random.randint(0,size-1)][random.randint(0,size-1)]=lgra
    i-=1
save(world)
