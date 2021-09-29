import operaciones_vectoriales as cal

def volumen(u,v,w):
  prod_cruz_vw = cal.prod_cruz(v, w)
  return abs(cal.prod_punto(u, prod_cruz_vw))

def area(u,v,w):
  prod_cruz_uv = cal.prod_cruz(u, v)
  prod_cruz_uw = cal.prod_cruz(u, w)
  prod_cruz_vw = cal.prod_cruz(v, w)
  norma_uv = cal.norma(prod_cruz_uv)
  norma_uw = cal.norma(prod_cruz_uw)
  norma_vw = cal.norma(prod_cruz_vw)
  return 2*(norma_uv + norma_uw + norma_vw)