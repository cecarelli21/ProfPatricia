print("Tabuada com For")

# num = 5
# tabuada = 1 * num
# print(num, "X", "1", "=", tabuada)
#
# tabuada = 2 * num
# print(num, "X", "2", "=", tabuada)

num = int(input("Entre com o numero da tabuada: "))
for i in range(1, 11):
    tabuada = i * num
    print(f"{num} X {i} = {tabuada}")


