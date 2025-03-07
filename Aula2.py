#Faça um algoritmo e pergunte a idade da pessoa e informe se ela pode entrar ou não (maior 18) caso ao contrário, informe para a pessoa que ela deve esperar mais alguns anos.

print("Qual a sua idade?")
idade = int(input())
if idade < 18:
    print("você não pode entrar na festa! E deve esperar mais alguns anos")
else:
    print("você esta autorizado entrar na festa")
