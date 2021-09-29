import math

pi = math.pi

def volumen(r, h):
  return h*pi*r**2

def area(r, h):
  return 2*pi*r**2 + 2*h*pi*r

def area_tapas(r):
  return 2*pi*r**2

def area_costado(r, h):
  return 2*h*pi*r

def formula_volumen():
  return 'hπr^2'

def formula_area():
  return '2πr^2 + 2hπr'