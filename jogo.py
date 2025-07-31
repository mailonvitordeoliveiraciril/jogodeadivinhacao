import random
print("###########################")
print("#    jogo de adivinhaçâo  #")
print("#  @mailonvitordeoliveira #")
print("###########################")
print("seja bem vindo ao jogo  🙃 ")

numeroSecreto= random.randrenge(0,100)
totaltentativas = 0
pontos = 100

print(" qual niveis de dificudade? ")
print("(1)- facil (2)- medio (3)- dificil")

nivel = int(input("Escolha um nivel:  "));

if(nivel == 1):
    print("20 tentativas")
    totaltentativas = 20
elif(nivel == 2)
    print("10 tentativas")
elif("nivel == 3"):
    print("5 tentativas ")
