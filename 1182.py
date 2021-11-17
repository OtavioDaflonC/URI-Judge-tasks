#1182 MATRIZES
n = int(input())
t = input()
  

m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)
       

if t == 'S':
    soma = 0
    for k in range(12):
        soma = soma + m[k][n]
    print(soma)
if t == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma += m[k][n]
    med= soma/12
    print('%.1f' % med)
