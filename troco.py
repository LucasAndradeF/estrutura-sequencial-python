valor_unitario = float(input("Informe o preço unitário do produto: "))
quantidade = int(input("Informe a quantidade comprada: "))
dinheiro_recebido = float(input("Informe o valor de pagamento: "))

valor_total = valor_unitario * quantidade
troco = dinheiro_recebido - valor_total

print(f"\nTroco: R${troco: .2f}")