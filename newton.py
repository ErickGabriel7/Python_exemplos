#Universidade Federal Rural de Pernambuco
#Unidade Acadêmica do Cabo de Santo Agostinho
#Monitoria de Linguagem de Programação
#Exemplo aplicado a Cálculo numérico
#Erick Gabriel de Lima Silva

from sympy import *
import matplotlib.pyplot as plt

print("POLINÔMIO INTERPOLADOR DE NEWTON")

x = []
y = []
repetir = True

k = 1
while repetir:
    print("Digite a coordenada x do ", k, "º ponto:")
    xe = float(input(">>>"))
    print("Digite a coordenada y do ", k, "º ponto:")
    ye = float(input(">>>"))
    adc = input("Você deseja adicionar mais um ponto? Digite 's' para sim e 'n' para não:\n>>>")
    x.append(xe)
    y.append(ye)
    if adc == "s" or adc == "S":
        k+=1
    elif adc == 'n' or adc == "N":
        break
    else:
        print("Entrada inválida, tente novamente")


def f(xn, xm):
    global y
    return ( (y[xm]-y[xn])/ (y[xm]-y[0]))
ordem = []
n = 0
while n < len(x):
    if n == 0:
        ordem.append(y[0])
    else:
        ordem.append(f(n-1,n))
    n+=1
x = symbols('x')
def P(x):
    #x = symbols('x')
    global ordem
    P = 0
    n = 0
    while n < len(ordem):
        P += (x**n)*ordem[n]
        n+=1
    return P
print("\nRESULTADO>>> ",P(x))

print("Para a plotar, forneça alguns dados sobre o intervalo do gráfico\n")

a = []
P_a =[]
c = int(input("Digite o menor número do eixo x do gráfico\n>>>"))
d = int(input("Digite o maior número do eixo x do gráfico\n>>>"))
passo = float(input("Digite o intervalo entre um ponto e outro no gráfico\n>>>"))
while c <= d:
    a.append(c)
    P_a.append(P(c))
    c+=passo

plt.plot(a,P_a, label="P(x)")
plt.title("Polinômio interpolador de Newton")
plt.grid()
plt.legend()
plt.show()