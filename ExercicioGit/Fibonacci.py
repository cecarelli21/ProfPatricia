titulo = "Fibo"
print(f"{titulo:^30}")

# termo = 8
# prim = 0
# seg = 1
# print(prim)
# print(seg)
# i = 2
# while i < termo:
#     soma = prim + seg
#     print(soma)
#     prim = seg
#     seg = soma
#     i += 1

termo = int(input("Entre com o nro de termos do Fibonacci: "))
prim = 0
seg = 1
if termo == 1:
    print(prim, end = ' ')
elif termo >= 2:
    print(prim, end = ' ')
    print(seg, end = ' ')
    i = 2
    while i < termo:
        soma = prim + seg
        print(soma, end = ' ')
        prim, seg = seg, soma
        i += 1
else:
    print("Numero de termos invalido")
