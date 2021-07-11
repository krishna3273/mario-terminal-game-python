from enemies import enemy
class mushroom(enemy):
    def __init__(self,x,y,c):
        super().__init__(x,y,c)
        self.mv1=-2