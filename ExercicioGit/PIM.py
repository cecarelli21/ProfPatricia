titulo = "Jogo do Pim FOR"
print(f"{titulo:^30}")

for i in range(1, 31):
    if i % 4 == 0:
        print("PIM")
    else:
        print(i)

titulo = "Jogo do Pim WHILE"
print(f"{titulo:^30}")

i = 1
while i <= 30:
    if i % 4 == 0:
        print("PIM", end = ' ')
        #print("PIM")
    else:
        print(i, end = ' ')
        #print(i)
    i += 1
