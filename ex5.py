import random
sorteados = []
for i in range(1,6):
    
    while True:
        aleat = random.randint(1,15)
        if aleat not in sorteados:
                print(f"[{aleat}]")
                sorteados.append(aleat)
                break
    