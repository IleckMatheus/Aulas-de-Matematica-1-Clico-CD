"""

Exercicio 2: Escrever código Python para ler através do console as variáveis:
“funcionário”,o nomedo funcionário de uma empresa;
“idade”, aidadedo funcionário;
“endereço”, oendereço do  funcionário;
a variável “função”, o cargo do funcionário e
a variável “salário”, o valor do seu salário. 
Utilizar o comando print paramostrar os resultados no console.Reajustar o salário lido em 20% e mostrar o seu valor atualizado no console.

"""

funcionario = input("Digite o nome do funcionário: ")

idade = int(input("\nDigite a idade do funcionário: "))

endereco = input("\nDigite o endereço do funcionário: ")

funcao = input("\nDigite a Função do funcionário: ")

salario = float(input("\nDigite o salário do funcionário: "))

print("\n ========================================================== \n")


print("O nome do funcionário é: ",funcionario)

print("\nA idade do funcionário é: ",idade)

print("\nO endereço do funcionário é: ",endereco)

print("\nA função do funcionário é: ",funcao)

print("\n O salário é : ",salario)

print("\n ================================== \n")

print("O salário do funcionário teve uma mudança de 20% \n")

mudanca = salario * 0.20

print("Mudança de 20% deu um total de: ", mudanca)

total = salario + mudanca

print("\nO valor novo do salário é de: ",total)
