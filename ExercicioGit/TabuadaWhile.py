titulo = "Tabuada While"
print(f"{titulo:^30}")

num = int(input("Entre com o numero da tabuada: "))
i = 1
while i <= 10:
    tabuada = i * num
    print(f"{num} X {i} = {tabuada}")
#    print(f"{num} X {i} = {i * num}")
    i += 1

