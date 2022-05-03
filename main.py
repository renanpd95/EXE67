import os

cont=0
for i in range(16):
  
  marca = str(input("Digite a marca do carro: "))
  model = str(input("Digite o modelo do carro: "))
  corCarro = str(input("Digite a cor do carro: "))
  os.system('clear')
  
  if ( corCarro == "azul" or corCarro == "Azul" or corCarro == "AZUL" or corCarro == "blue"):
    cont = cont+1
else:
  print("A quantidade de carros azul é: ",cont)
