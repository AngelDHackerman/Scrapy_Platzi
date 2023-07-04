def even_numbers():
  n = 0
  for _ in range(100):
    yield n
    n += 2

# Crear el generador
my_gen = even_numbers()

# Imprimir los primeros 100 números pares
for number in my_gen:
  print(number)
