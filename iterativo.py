vetor = []
entrada = input().split()

for k in entrada:
    k = int(k)
    vetor.append(k)

def soma_vetor(vetor):
    resultado = 0
    for i in vetor:
        resultado = resultado + i 
    return resultado

print(soma_vetor(vetor))      


