#2724   ATENÇÃO: ESSA É UMA PRIMEIRA VERSÃO DO CÓDIGO E AINDA NÃO COBRE TODAS AS CIRCUNSTÂNCIAS TESTADAS NO URIJUDGE
N= int(input())
for i in range(N):
  t= int(input())
  lista=[]
  for j in range(t):
    per= input()
    lista.append(per)
  lista2=[]
  p= int(input())
  for k in range(p):
    exp=input()
    lista2.append(exp)
 
  for y in lista2:
    if 'Mg2F' in y:
      teste=y.find('Mg2F')
      coisa=y[teste +len(Mg2F)]
      cont = [0]
      if coisa.isupper():
          cont += [1]

#em vez de usar in, usar o find: função de uma string, onde a variável nomeada terá o index das string aplicada na função
