medida_a = float(input("Informe a medida A: "))
medida_b = float(input("Informe a medida B: "))
medida_c = float(input("Informe a medida C: "))

area_quadrado = medida_a * medida_a
area_triangulo = (medida_a * medida_b) / 2
area_trapezio = (medida_a + medida_b) / 2 * medida_c

print(f"\nÁrea do quadrado: {area_quadrado: .4f} \nÁrea do triângulo: {area_triangulo: .4f} \nÁrea do trapézio: {area_trapezio: .4f}")