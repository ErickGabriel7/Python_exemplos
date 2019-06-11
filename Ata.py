#Universidade Federal Rural de Pernambuco
#Unidade Acadêmica do Cabo de Santo Agostinho
#Monitoria de Linguagem de Programação
#Exemplo do uso de arquivos - Ata de presença
#Erick Gabriel de Lima Silva

print("ATA")

#Obtendo a data da aula
data=input("Digite a data da aula(DD-MM-AA): ")

#Gerando o arquivo e abrindo-o no modo write
ata=open("Ata do dia "+str(data)+".txt", "w")
#Escrevendo no arquivo a data da aula
ata.write("Esta ata refere-se ao dia ")
ata.write(data+"\n")

#Obtendo e escrevendo no arquivo a disciplina
disciplina=input("Digite o nome da disciplina: ")
ata.write("Disciplina: ")
ata.write(disciplina+"\n")

#Obtenção do nome dos alunos e escrevendo-os
#no arquivo
u=False
nome=""
while u ==False:
    nome=input("Digite seu nome: ")
    ata.write(nome + "\n")
    a=input("Voce e o ultimo a assinar? ")
    if a == "sim" or a=="Sim" or a=="s":
        u=True
    else:
        u=False
ata.close()