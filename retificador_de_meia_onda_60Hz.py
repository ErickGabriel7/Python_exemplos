#Universidade Federal Rural de Pernambuco
#Unidade Acadêmica do Cabo de Santo Agostinho
#Eletronica 1
#Processamento dos dados experimentais e teoricos
#Erick Gabriel de Lima Silva

import csv
import matplotlib.pyplot as plt

v_osc = []
t_osc = []
v_sim = []
t_sim = []

#arquivo que contem os dados obtidos do osciloscopio
with open("60Hz_osc.csv", "r") as osc:
    cont = csv.reader(osc, delimiter=",")
    for k in cont:
        t_osc.append(float(k[3]))
        v_osc.append((float(k[4])))

#arquivo que contem os dados obtidos no simulador
with open ("60Hzcerto","r") as sim:
    cont_sim = csv.reader(sim, delimiter=",")
    cont_sim = list(cont_sim)
    cont_sim.remove(["time	V(n002)"])
    for k in cont_sim:
        k[0] = (k[0]).split("\t")
    for k in cont_sim:
        t_sim.append(k[0][0])
        v_sim.append(k[0][1])
    c = 0
    while c < len(t_sim):
        t_sim[c] = float(t_sim[c])
        v_sim[c] = float(v_sim[c])
        c += 1

#ajuste na escala de tempo
t_osc_certo = []
for k in t_osc:
    t_osc_certo.append(k+0.0185)

plt.plot(t_osc_certo,v_osc, label="V(t) experimental")
plt.plot(t_sim,v_sim, label="V(t) simulado", color="r")
plt.xlabel("t(s)")
plt.ylabel("v(V)")
plt.legend()
plt.grid()
plt.title("Retificador de meia onda (f = 60Hz) ")
plt.show()
