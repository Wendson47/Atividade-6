quantidade = float(input("Digite quantos itens diferentes: "))
itens = []
i = 0
while i < quantidade:
    nome = input("Nome do item " + str(i+1) + ": ")
    quantidade = input("quantidade do item " + str(i+1) + ": ")
    valor = float(input("Qual o valor do item " + str(i+1) + ": "))
    nome = input("Nome do item " + str(i+2) + ": ")
    quantidade = input("quantidade do item " + str(i+2) + ": ")
    valor = float(input("Qual o valor do item " + str(i+2) + ": "))
    valorItem = {
       "nome" : nome,
       "quantidade" : quantidade,
       "valor" : valor
    }
    itens.append(valorItem)
    i += 1
    print(itens)
    soma = valor + valor
    soma += valor
    print(soma)

