#Faça um algoritmo e pergunte a idade da pessoa e informe se ela pode entrar ou não (maior 18) caso ao contrário, informe para a pessoa que ela deve esperar mais alguns anos.

print("Qual a sua idade?")
idade = int(input())
tempo = 18 - idade
if idade < 18:
    print("Você não esta autorizado entrar na festa, espere:", tempo ,"anos")

else:
    print("Você esta autorizado entrar na festa")
