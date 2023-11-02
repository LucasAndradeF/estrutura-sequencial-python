largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite comprime do terreno: "))
valor_m_quadrado = float(input("Digite valor do metro quadrado: "))

area_terreno = largura_terreno * comprimento_terreno
preco_terreno = valor_m_quadrado * area_terreno

print(f"Área do terreno: {area_terreno: .2f} m²")
print(f"Preço do terreno: R${preco_terreno: .2f}")

