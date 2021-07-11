from board import list
from characters import character
class enemy(character):
    def  __init__(self,x,y,c):
        self.mv1=-1
        super().__init__(x,y,c,-1)
    def move(self,a,b):
        '''if list[self.y+a][self.x+b]==' ' or list[self.y+a][self.x+b]=="M":
            list[self.y][self.x]=' '
            self.y=self.y+a
            self.x=self.x+b
            list[self.y][self.x]="O"'''
        if super().move(a,b,[" ","m","M"])==True:
            a+=0
        else:
            self.mv=0-self.mv
    def fall(self):
        if (list[self.y-1][self.x]==' ' and self.y!=0):
            #and (self.status==False or self.y==6)
            self.move(self.mv1,0)
            return True
        if(self.y==0) :
            list[self.y][self.x]=" "
            self.mv1=0
            self.mv=0
            return False
    def inrange(self,start,stop):
        if(self.x<=stop and self.x>=start):
            if  self.fall()!=False:
                if self.x==0:
                    self.mv=0-self.mv
                self.move(0,self.mv)

