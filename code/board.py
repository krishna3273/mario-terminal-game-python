from colorama import Fore,Style
list=[[" " for i in range(0,600)] for i in range(0,40)]
list1=[3,3,3,3,3,3,3,4,6,4,6,4,6,4,6,4,6,3,3,3,25,9,3,3,6,3,3,3,3,3,9,3,3,3,3,6,4,6,4,6,4,3,1,1,4,3,3,15,3,3]
list2=[2,2,2,2,2,2,2,3,2,5,2,6,2,6,2,6,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,4,2,6,2,20,1,2,6,6,3,3,3]
list3=['?','-','?','-','?','?',"-",'c','c','c','c','c','c','c','c',' ',' ','-','?','-','-','-','?','-','-','?','?','?','?','-','-','-','?','-','?','-','c','c','c','c',' ','G','a','O','d','c','c','c','c','c']
list4=[32,41,44,47,47,50,53,70,69,100,99,130,129,180,179,210,260,230,233,236,237,270,279,279,292,306,314,314,322,333,338,353,356,359,362,356,440,439,484,483,418,525,526,526,527,533,545,533,533,545]
list5=[12,12,12,12,16,12,12,6,9,6,11,6,12,6,12,0,0,12,12,12,16,16,16,12,12,12,12,16,12,12,16,16,16,16,16,12,6,10,6,10,0,6,8,28,27,6,6,12,15,15]
start=0
stop=135
class board:
    def __init__(self,width,height,start,stop):
        self.width=width
        self.height=height
        self.start=start
        self.stop=stop
    def cloud(self,list):
        for j in range(10):
                list[38][8+30*j]='^'
                list[37][7+30*j]='('
                list[37][9+30*j]=')'
                list[36][6+30*j]='('
                list[36][10+30*j]=')'
                list[35][5+30*j]='('
                list[35][11+30*j]=')'
                list[34][4+30*j]='<'
                list[34][12+30*j]='>'
                for i in range(5,12):
                    list[34][i+30*j]='_'
    def printboard(self,lives,score,ti,coins):
        print(Fore.WHITE+"SCORE:"+str(score)+"                        ",end=" ")
        print(Fore.WHITE+" TIME:"+str(ti)+"                           ",end=" ")
        print(Fore.WHITE+"LIVES:"+str(lives)+"                        ",end=" ")
        print(Fore.WHITE+"COINS:"+str(coins)+"                        ",end="\n")
        self.cloud(list)
        for i in range(0,self.height):
            for j in range(self.start,self.stop):
                if list[self.height-i-1][j] in ['?','-']:
                    print(Fore.RED+list[self.height-i-1][j],end='')
                elif  list[self.height-i-1][j] in ['c']:
                    print(Fore.GREEN+list[self.height-i-1][j],end='')
                elif  list[self.height-i-1][j] in ['*']:
                    print(Fore.MAGENTA+list[self.height-i-1][j],end='')
                elif  list[self.height-i-1][j] in ['A','G']:
                    print(Fore.YELLOW+list[self.height-i-1][j],end='')
                elif  list[self.height-i-1][j] in ['E']:
                    print(Fore.BLUE+list[self.height-i-1][j],end='')
                else:
                    print(Fore.WHITE+list[self.height-i-1][j],end='')
            print(end="\n")

    def createblock(self,w,l,c,x,y):
        for i in range(y,y+l):
            for j in range(x,x+w):
                list[i][j]=c
    def createbackground(self):
        for i in range(0,6):
            for j in range(0,self.width):
                list[i][j]='*'
        for i in range(0,len(list1)):
            self.createblock(list1[i],list2[i],list3[i],list4[i],list5[i])

        
        k=0
        for i in range(6,10):
            for j in range(0,4):
                if 362+k+2*j<=368:
                    self.createblock(2,2,'G',362+k+2*j,2*i-6)
            k+=2
        k=0
        for i in range(6,10):
            for j in range(0,4):
                if 388-k-2*j>=382:
                    self.createblock(2,2,'A',386-k-2*j,2*i-6)
            k+=2
        k=0
        for i in range(6,10):
            for j in range(0,4):
                if 410+k+2*j<=416:
                    self.createblock(2,2,'G',410+k+2*j,2*i-6)
            k+=2
        
        #self.createblock(4,6,' ',418,0)

        k=0
        for i in range(6,10):
            for j in range(0,4):
                if 422+k+2*j<=428:
                    self.createblock(2,2,'G',422+k+2*j,2*i-6)
            k+=2

        

        k=0
        for i in range(6,13):
            for j in range(0,9):
                if 490+k+2*j<=506:
                    self.createblock(2,2,'G',490+k+2*j,2*i-6)
            k+=2



'''c=board(1300,40,600,730)
c.createbackground()
c.printboard(0,0,0,0)'''
