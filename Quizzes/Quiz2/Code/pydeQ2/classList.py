
# y: layer shows seniority

class oldBot:
    x = 300 #pos 
    y = 40
    def __init__(self,name,cloth,type):
        self.buildHead(type)
        self.buildBody(name,cloth)
    def buildHead(self,type):
        fill(255)
        stroke(0)
        strokeWeight(1)
        if type == 'a':
            square(self.x-25, self.y-10, 50)
        elif type =='b':
            ellipse(self.x, self.y+10, 60, 60) 
        elif type =='c':
            triangle(self.x,self.y+40,self.x-40,self.y-10,self.x+40,self.y-10)  
    def buildBody(self,name,cloth):
        stroke(0)
        strokeWeight(12)
        line(self.x-40, self.y+50, self.x-55, self.y+120) #--arms
        line(self.x+40, self.y+50, self.x+55, self.y+120)
        noStroke()
        fill (cloth)
        rect(self.x-40,self.y+40,80,80) #body
        fill(0)
        ellipse(self.x-15, self.y+5, 18, 18) #---------eyes
        ellipse(self.x+15, self.y+5, 18, 18) 
        textSize(20)
        fill(0)
        font = loadFont("Arial-Black-48.vlw") #-------name 
        text(name,self.x-40,self.y+140)

class the2(oldBot):
    y = 220
    x = 60
    def __init__(self,name,cloth,type,pattern,relate,twoParents,parent):
        self.relationShip(relate,twoParents,parent)
        oldBot.__init__(self,name,cloth,type)
        self.clothpattern(pattern)
    def clothpattern(self,pattern):# ------------set cloth pattern
        if pattern != 0:
            img = loadImage(str(pattern)+'.png') 
            image(img,self.x-40,self.y+40)
        else: #---------------------------------no pattern
            print('none')
    def relationShip(self,relate,twoParents,parent): #----------------------draw line relation
        if relate:
            stroke(200)
            strokeWeight(4)
            line (parent.x,parent.y+100,self.x,self.y)
            if twoParents :
                line (parent.x-120,parent.y+100,self.x,self.y)
    


class the3(the2):
    y = 400
    x = 60
    def __init__(self,name,cloth,type,pattern,relate,twoParents,parent,posX):
        self.x=posX
        the2.__init__(self,name,cloth,type,pattern,relate,twoParents,parent)
    def flash(self):
        fill(int(random(0,255)))
        ellipse(self.x-15, self.y+5, 20, 20) 
        ellipse(self.x+15, self.y+5, 20, 20) 
