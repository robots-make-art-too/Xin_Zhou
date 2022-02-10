S = list []
BH = list []
NB_S,NB_BH
NUM_COLOR

def setup():
    size(600,600)
    background(0)
    strokeWeight(1)
    colorMode(HSB,360)
    
    NUM_COLOR = 0
    
    NB_S = 2500
    NB_BH = 3
    
    R = 300
    for s in range(NB_S):
        S[s]=creatVector(cos(s)*R,sin(s)*R)
    for bh in range(NB_BH):
        BH[bh] = creatVector(random(-R,R),random(-R,R))
        
def draw():
    translate(width/2,height/2)
    NUM_COLOR = ( NUM_COLOR + 3 )%360
    stroke(NUM_COLOR, 360, 360)
    
    for s in range(NB_S):
        S_X = S[s].x
        S_Y = S[s].y
        
        direction = 0.0
        for bh in range(NB_BH):
            direction += atan2( BH[bh].y - S_Y, BH[bh].x - S_X ) * 2 
        
        MOVE = createVector(5,0)
        MOVE.rotate(direction)
        S[s] = S[s].add(MOVE)   
        
        line(S_X, S_Y, S[s].x, S[s].y)
    if mouseIsPressed:
        setup()
        
        
