from board import list
class character:
    def  __init__(self,x,y,c,mv):
        self.x=x
        self.y=y
        self.mv=mv
        self.c=c
        list[y][x]=c
    def move(self,a,b,l):
        #if list[self.y+a][self.x+b]==' ' or list[self.y+a][self.x+b]=="M":
        if list[self.y+a][self.x+b] in l:
            list[self.y][self.x]=' '
            self.y=self.y+a
            self.x=self.x+b
            list[self.y][self.x]=self.c
            return True
        return False