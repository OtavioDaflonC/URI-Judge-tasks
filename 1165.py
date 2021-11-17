#1165
n = int(input('Quantos números vou rodar?'))
print('moleza...')
for i in range(0,n):
    num = int(input())
    crit = 0
    deno=1
    while deno <= num:
        if num % deno == 0:
            crit = crit + 1
        deno = deno + 1
    if crit > 2:
        print(num,'nao eh primo')
    else:
        print(num,'eh primo')
print('foi.','Não tem um mais difícil não?')
