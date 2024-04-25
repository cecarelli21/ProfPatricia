import time
titulo = "Contagem regressiva"
print(f"{titulo:^30}")

for cont in range(60,-1,-1):
    time.sleep(1)
    print(cont)
