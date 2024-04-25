titulo = "Divisiveis por 5"
print(f"{titulo:^30}")

num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))

if num1 > num2:
    # temp = num1
    # num1 = num2
    # num2 = temp

    num1, num2 = num2, num1

print(f"numeros divisiveis por 5 entre {num1} e {num2}:")
for i in range(num1, num2 + 1):
    if i % 5 == 0:
        print(i, end=' ')
