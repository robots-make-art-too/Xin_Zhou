def setup():
    size(500,400)
    background(128,128,255)
    noStroke()
def draw():
    for i in range(5):
        sizeElli = random(10,500)
    
        fill (255,255,255,3)
        ellipse(random(width),random(height), sizeElli,sizeElli)
        
        fill(96,96,255,5)
        ellipse(random(width),random(height),sizeElli,sizeElli)
