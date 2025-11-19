MIN, MAX = 0.0, 5.0
notas = []

print("Ingrese las notas (escriba 'fin' para terminar):")

while True:
    entrada = input("Nota: ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        if MIN <= nota <= MAX:
            notas.append(nota)
        else:
            print("Nota fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

if notas:
    print(f"\Total: {len(notas)} | Promedio: {sum(notas)/len(notas):.2f} | "
          f"Máx: {max(notas)} | Mín: {min(notas)}")
else:
    print("No se registraron calificaciones válidas.")