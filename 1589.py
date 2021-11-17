#1589
# o menor raio é a soma dos dois raios r1 e r2.
t=int(input())

for i in range(t):
  R=input()
  r1,r2=map(int,R.split())
  print(r1 + r2)
