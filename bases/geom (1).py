
class Point :
    def milieu(self,p) :
        return Point((self.x+p.x)/2,(self.y+p.y)/2)
    def __repr__(self) :
       return 'Point('+str(self.x)+','+str(self.y)+')'	
 
    def mediatrice(self,p) :
        if self.y==p.y : return None
        m=self.milieu(p)
        co=(p.x-self.x)/(p.y-self.y)
        a=-co
        b=m.x*co+m.y
        return Droite(a,b)

    def __init__(self,x,y) :
        self.x=x
        self.y=y
 

class Droite :
    def __init__(self,a,b) :
        self.a=a
        self.b=b
    def appartient(self,p) :
        if p.y==self.a*p.x+self.b : return True
        return False
    def prendPoint(self,x) :
        y=self.a*x+self.b
        return Point(x,y)
    def __repr__(self) :
        return 'Droite('+str(self.a)+','+str(self.b)+')'
    def parallele(self,p) :
        d=Droite(self.a,self.b)
        d.b=p.y-d.a*p.x
        return d	

class PointCouleur(Point) :
    def __init__(self,x,y,col) :
        super().__init__(x,y)
        self.col=col
    def __repr__(self) :
        return 'PointCouleur('+repr(self.x)+','+repr(self.y)+','+repr(self.col)+')'