#1064
lista=[]
count=0
for i in range(6):
  n=float(input())
  if n > 0 :
    count += 1
    lista.append(n)
  else:
    continue
media=sum(lista)/count
print(count,'valores positivos')
print('%.1f' % media)
  
