salario_pessoa = float

nome_pessoa = input("Informe o seu nome: ")
valor_hora = float(input("Informe o valor por hora: "))
horas_trabalhadas = int(input("Informe as horas trabalhadas: "))

salario_pessoa = valor_hora * horas_trabalhadas

print(f"\nO pagamento de {nome_pessoa} deve ser R${salario_pessoa: .2f}")
