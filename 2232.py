#2232
t = int(input())
while t:
    t -= 1
    #subtrai uma quantidade de jeito mais eficiente
    n = int(input())
    soma = (1 << n) - 1
    # 1<<n será o mesmo que 1*2^n, que é exatamente oq preciso no problema como foi dito
    print(soma)
