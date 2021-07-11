from board import list,list1,list2,list3,list4,list5
import sys
from characters import character
class mario(character):
    def  __init__(self,x,y,c):
        '''self.x=x
        self.y=y
        self.mv=1
        list[y][x]="M"'''
        self.score=0
        self.coins=0
        self.steps=0
        self.bo=True
        self.status=True
        self.lives=3
        super().__init__(x,y,c,1)
    
    def move(self,a,b):
        '''if list[self.y+a][self.x+b]==' ':
            list[self.y][self.x]=' '
            self.y=self.y+a
            self.x=self.x+b
            list[self.y][self.x]='M'
            #self.steps=self.steps+1'''
        super().move(a,b,[" "])
    def findandchange(self,x,y,c):
        ind=0
        for i in range(0,45):
            if (list4[i] <= x and list4[i]+list1[i]>x) and list5[i]==y:
                ind=i
                break
        for i in range(list5[ind],list5[ind]+list2[ind]):
            for j in range(list4[ind],list4[ind]+list1[ind]):
                list[i][j]=c
        return ind
    def jump(self,limit):
        r=-1
        if list[self.y+self.mv][self.x]!=' ':
            if self.mv==-1:
                self.bo=True
                self.mv=1
                self.steps=0
                if self.y!=6:
                    self.status=False
                else:
                    self.status=True
            else:
                #self.bo=True
                if list[self.y+self.mv][self.x]=='-' and self.c=="M":
                    ind=self.findandchange(self.x,self.y+self.mv," ")
                    return -100
                elif list[self.y+self.mv][self.x]=='?':
                    ind=self.findandchange(self.x,self.y+self.mv,"*")
                    r=ind
                #mushroom(list4[ind],list2[ind]+list5[ind],"P")
                self.mv=-1
        elif (self.y==22 or self.steps==limit):
            self.mv=-1
            self.move(self.mv,0)
            self.steps=1
        else:
            self.move(self.mv,0)
            self.steps+=1
        return r
    def fall(self):
        if (list[self.y-1][self.x]==' ' and (self.status==False or self.y==6) and (list[self.y-1][self.x-1]!=" " or list[self.y-1][self.x+1]!=" ") ):
            self.bo=False
            self.mv=-1
            return True
        if(self.y==0) or list[self.y][self.x]=="O" :
            list[self.y][self.x]=" "
            self.x=10
            self.y=6
            list[6][10]="m"
            return False
