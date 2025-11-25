 def ganancia_maxima(i, a):
 # Caso base: no hay oferentes
 if i == 0:
 return 0
   
 # Opcion 1: no asignar acciones al oferente i
 mejor = ganancia_maxima(i- 1, a)
 # Opcion 2: asignar x acciones al oferente i, con l[i] <= x <= min(u[i], a)
 if a >= l[i]:
 limite_superior = min(u[i], a)
 for x in range(l[i], limite_superior + 1):
 valor = p[i] * x + ganancia_maxima(i- 1, a
x)
 if valor > mejor:
 mejor = valor
 return mejor
