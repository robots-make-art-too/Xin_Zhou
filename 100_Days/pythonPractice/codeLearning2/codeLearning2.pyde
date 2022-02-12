numPoints = 500
incr = TWO_PI/numPoints
r1, r2, r3, r4, n1, n2, n3, n4, phi1, phi2, phi3, phi4

def setup():
  size(550, 550)
  r1 = r2 = 78
  r3 = 52
  r4 = 39
  n1 = 3
  n2 = -13
  n3 = 11
  n4 = 19
  phi2 = phi3 = phi4 = random(PI)
  strokeWeight(1.5)


def draw():
  background(240)
  phi1 += .0022

  noStroke()
  fill(0, 25)
  translate(width/2+7, height/2+7)
  beginShape()
  for i in range(TWO_PI,incr):
    x = r1 * cos (n1 * (i + phi1)) + r2 * cos(n2*(i + phi2)) + r3 * cos(n3*(i+phi3)) + r4 * cos(n4*(i+phi4))
    y = r1 * sin (n1 * (i + phi1)) + r2 * sin(n2*(i + phi2)) + r3 * sin(n3*(i+phi3)) + r4 * sin(n4*(i+phi4))
    vertex(x, y)

  endShape(CLOSE)

  stroke(#FFC30E)
  fill(60)
  translate(-7, -7)
  beginShape()
  for i in range(TWO_PI):
    x = r1 * cos (n1 * (i + phi1)) + r2 * cos(n2*(i + phi2)) + r3 * cos(n3*(i+phi3)) + r4 * cos(n4*(i+phi4))
    y = r1 * sin (n1 * (i + phi1)) + r2 * sin(n2*(i + phi2)) + r3 * sin(n3*(i+phi3)) + r4 * sin(n4*(i+phi4))
    vertex(x, y)

  endShape(CLOSE)
