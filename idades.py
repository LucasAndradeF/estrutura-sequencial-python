media_idade = float

nome_pessoa_um = input("Informe o seu nome: ")
idade_pessoa_um = int(input("Informe a sua idade: "))
nome_pessoa_dois = input("Informe o seu nome: ")
idade_pessoa_dois = int(input("Informe a sua idade: "))

media_idade = (idade_pessoa_um + idade_pessoa_dois) / 2

print(f"\nDados da primeira pessoa: \nNome: {nome_pessoa_um} \nIdade: {idade_pessoa_um}")
print(f"\nDados da segunda pessoa: \nNome:  {nome_pessoa_dois} \nIdade: {idade_pessoa_dois}")
print(f"\nA idade média de {nome_pessoa_um} e {nome_pessoa_dois} é de {media_idade} anos.")

