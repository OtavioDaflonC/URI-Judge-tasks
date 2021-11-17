#1015   
xya = input().split(" ")
xyb = input().split(" ")
#split no início permite por mais de 1 valor no input(lembre que vc precisa dizer entre parênteses
#o caractér que irá ser splitado, nesse caso, o espaço)
x1,y1=xya
x2,y2=xyb
#aqui podemos nomear várias variáveis juntas, já que xya e xyb agora são listas.
# e cada variável é assimilada com seu respectivo index.
resp= ((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)**(1/2)

print('%.4f' % resp)
