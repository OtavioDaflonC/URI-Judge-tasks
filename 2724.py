#2724   ATENÇÃO: ESSA É UMA PRIMEIRA VERSÃO DO CÓDIGO E AINDA NÃO COBRE TODAS AS CIRCUNSTÂNCIAS TESTADAS NO URIJUDGE
N= int(input())

for i in range(N):
  T= int(input())
  lista=[]
  for t in range(T):
    per= input()
    lista.append(per)
  lista2=[]
  p= int(input())
  for k in range(p):
    exp=input()
    lista2.append(exp)
 
#Trecho de análise:
    #análise genérica    
    #se o elemento perigoso está dentro da lista de experimentos
for n in range(N):
  for y in lista2:
    
  
    for x in lista:
        if x == y:
          print('Abortar')
          
          break
        elif x in y:
          try:
            teste=y.find(x)
            coisa=y[teste +(len(x))]
            if coisa.isupper():
                print ('Abortar')
                
                break
            elif coisa.islower():
                    continue
            elif coisa.isnumeric():
                    print ('Prossiga')
                    break
          except IndexError:
            print('Prossiga')
            break
    
    else:
      print('Prossiga')
  print('')   

