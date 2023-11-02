conversor = int(input("Informe a duração em segundos: "))

horas = conversor // 3600
minutos = (conversor % 3600) // 60
segundos = conversor % 60

print(f"Resultado: {horas}: {minutos}: {segundos}.")