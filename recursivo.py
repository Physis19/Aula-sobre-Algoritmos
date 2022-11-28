vetor = []
entrada = input().split()

for k in entrada:
    k = int(k)
    vetor.append(k)

posicao_vetor = len(vetor) - 1 #sem o subtrair, ele vai buscar um índice maior do que o existente na lista


def soma_vetor(x, vetor):
    if x < 0:
        return 0
    
    else:
        return vetor[x] + soma_vetor(x -1, vetor)
    
print(soma_vetor(posicao_vetor, vetor))

