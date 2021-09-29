
def norma(a):
  return (a[0]**2 + a[1]**2 + a[2]**2)**(0.5)

def suma(a, b):
  return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def prod_punto(a, b):
  return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def prod_cruz(a, b):
  x = a[1]*b[2] - a[2]*b[1]
  y = a[2]*b[0] - a[0]*b[2]
  z = a[0]*b[1] - a[1]*b[0]
  return [x, y, z] 