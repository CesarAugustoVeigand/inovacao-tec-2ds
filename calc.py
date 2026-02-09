# 1. Solicita os 4 números via input e os armazena em uma lista
numeros = []
for i in range(4):
    valor = input(f"Digite o {i+1}º número: ")
    # 2. Converte o valor para float e adiciona à lista
    numeros.append(float(valor))

# 3. Calcula a média somando os itens e dividindo pela quantidade
media = sum(numeros) / len(numeros)

# 4. Exibe o resultado formatado com duas casas decimais
print(f"A média dos números é: {media:.2f}")
