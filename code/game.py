from mario import mario
from board import board,list,start,stop,list1,list2,list3,list4,list5
import os
import time
import termios
import signal
import errno
import threading
import sys
import random as r
from functools import wraps
from enemies import enemy
from powerup import mushroom
from sound import play,SOUND_PATHS
TERMIOS = termios
timeout_value = 0.2
st=time.time()


def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


@timeout(0.2)
def getkey():
        start = time.time()
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0 
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c


def reset(E,E1,E2,boar,p,P):
    for j in range(len(E)):
        list[E[0].y][E[0].x]=" "
        list[p.y][p.x]=" "
        del E[0]
    for j in range(len(P)):
        list[P[0].y][P[0].x]=" "
        list[p.y][p.x]=" "
        del P[j]
    for j in range(len(E1)):
        E.append(enemy(E1[j],E2[j],"E"))
    boar.start=0
    boar.stop=135
    boar.createbackground()
    p.c="m"
    p.x=10
    p.y=6
    p.status=True
    p.mv=1
    p.steps=0
    p.lives-=1
    p.score=0
    p.coins=0
    list[6][10]="m"
    time.sleep(2)


boar=board(600,40,0,135)
boar.createbackground()
p=mario(10,6,"m")
E1=[25,115,233,245,275,276,295,296,332,334,338,340,464]
E2=[6,6,14,19,6,6,6,6,6,6,6,6,6]
E=[]
P=[]
for j in range(len(E1)):
    q=enemy(E1[j],E2[j],'E')
    E.append(q)
#print(list[6][20])
limit=9
#score=0
while True:
    if p.lives==0:
        os.system('clear')
        for i in range(0,15):
            print(end="\n")
        for i in range(0,50):
            print(end=" ")
        print("GAME OVER")
        for i in range(0,15):
            print(end="\n")
        play(SOUND_PATHS['gameover'])
        sys.exit()
    if p.x==524:
        list[p.y][524]=" "
        list[p.y][538]=p.c
        boar.printboard(p.lives,p.score,0,p.coins)
        play(SOUND_PATHS['stage'])
        sys.exit()
    
    try:
        k=getkey()
    except:
        k=None
    if k==b'q':
        sys.exit()
    if k==b'a':
        p.move(0,-1)
    if k==b'd':
        p.move(0,1)
    if (k==b'w' or k==b's') and p.bo==True:
        p.bo=False
        #limit=9
        if(k==b's'):
            limit=1
            play(SOUND_PATHS['jump-small'])
        if(k==b'w'): 
            limit=9
            play(SOUND_PATHS['jump-super'])
    else:
        if p.bo==False:
            r1=p.jump(limit)
            if r1!=-1:
                if r1==2 :
                    P.append(mushroom(list4[r1],list5[r1]+list2[r1],"P"))
                    play(SOUND_PATHS['powerup-appears'])
                if r1==-100:
                    play(SOUND_PATHS['breakblock'])
                if r1>=0:
                    p.score+=10
                    p.coins+=1
                    play(SOUND_PATHS['coin'])
    if(p.fall()==False):
        play(SOUND_PATHS['mariodie'])
        reset(E,E1,E2,boar,p,P)
    for j in range(len(E)):
        E[j].inrange(boar.start,boar.stop)
    for j in range(len(P)):
        P[j].inrange(boar.start,boar.stop)
    if(p.x>=(boar.start+boar.stop)/2):
        boar.start+=1
        start+=1
        stop+=1
        boar.stop+=1
    r=0
    for j in range(0,len(E)):
        if(p.mv!=-1 and E[j-r].x==p.x and E[j-r].y==p.y):
                if p.c=="m":
                    play(SOUND_PATHS['mariodie'])
                    reset(E,E1,E2,boar,p,P)
                if p.c=="M":
                    p.c="m"
                    p.x+=4
                    list[p.y][p.x]="m"
                    play(SOUND_PATHS['bump'])
        if(p.mv==-1 and E[j-r].x==p.x and E[j-r].y==p.y):    
            list[E[j-r].y][E[j-r].x]=p.c
            p.score+=30
            E.remove(E[j])
            r+=1
    r=0
    for j in range(0,len(P)):
        if( P[j-r].x==p.x and P[j-r].y==p.y):
            list[p.y][p.x]="M"
            p.c="M"
            play(SOUND_PATHS['powerup'])
            p.score+=100
            P.remove(P[j-r])
    now=time.time()
    time1=round(300-now+st)
    if time1==0:
        play(SOUND_PATHS['mariodie'])
        reset(E,E1,E2,boar,p,P)
        st=time.time()
    os.system('clear')
    boar.printboard(p.lives,p.score,time1,p.coins)
    #time.sleep(0.1)  