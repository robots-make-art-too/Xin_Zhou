def setup():
    size(150,150)

def draw():
    for i in range(18,-1,-1):
        if i%2==0:
            fill(0)
        else:
            fill(255)
           
        ellipse(width/2+8*sin(frameCount/12-i/2),height/2+8*cos(frameCount/12-i/2),15*i,15*i)
