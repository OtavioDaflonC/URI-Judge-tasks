#1253
n=int(input())

alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista_=list(alf)
for i in range(n):
    txt=input()
    key=int(input())
    
  
    lista=list(txt) 
    output=[]
    for elemento in lista:
        for letter in lista_:
            if letter == elemento:
                indexnovo=key + lista_.index(letter)
               
                alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                letter= lista_[indexnovo]
                output.append(letter)
              
                
            
                break
            else:
                continue
   
    criterio=''
    resp=criterio.join(output)
  
    print(resp)  
