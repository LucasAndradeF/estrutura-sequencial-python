distancia_km = float(input("Informe a quantidade percorrida em KM: "))
combustivel_gasto = float(input("Informe a quantidade de combustível gasto: "))

media_consumo = distancia_km / combustivel_gasto

print(f"\nConsumo médio: {media_consumo: .3f}")
