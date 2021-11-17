#2653

lista=[]
inf=0
while 1>inf:
  try:
    j=input()
    if j not in lista:
      lista.append(j)

    
  except EOFError:
    break
print(len(lista))
