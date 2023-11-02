import math

base_retangulo = float(input("Informe a base do retangulo: "))
altura_retangulo = float(input("Informe a altura do retangulo: "))

area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = 2 * (base_retangulo + altura_retangulo)
diagonal_retangulo = math.sqrt(base_retangulo**2 + altura_retangulo**2)

print(f"Área = {area_retangulo: .4f}")
print(f"Perimetro = {perimetro_retangulo: .4f}")
print(f"Diagonal = {diagonal_retangulo: .4f}")

