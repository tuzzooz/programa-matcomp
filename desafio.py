def letra_da_camada(i):
    if i < 26:
        return chr(ord('A') + i)  
    else:
        return chr(ord('a') + (i - 26)) 

def desenhar_camadas(N): 
    tamanho = 2 * N + 1 
    matriz = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]  

    for camada in range(N):
        letra = letra_da_camada(camada)
       
        for i in range(camada, tamanho - camada):
            matriz[camada][i] = letra           
            matriz[tamanho - camada - 1][i] = letra  
            matriz[i][camada] = letra           
            matriz[i][tamanho - camada - 1] = letra 


    centro = N
    matriz[centro][centro] = '*'

  
    for linha in matriz:
        print(' '.join(linha))

N = int(input("Digite o número de camadas (de 1 a 52): "))
desenhar_camadas(N)

