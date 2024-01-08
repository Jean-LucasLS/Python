cardapio = {
    'entrada': ['Salada', 'Sopa', 'Bruschetta'],
    'prato_principal': ['Bife com fritas', 'Lasanha', 'Peixe grelhado'],
    'sobremesa': ['Sorvete', 'Torta de chocolate', 'Frutas'],
    'bebida': ['Refrigerante', 'Suco', 'Água']
}

def exibir_cardapio():
    print("-------- Cardápio do Restaurante --------")
    print("Entradas:")
    for item in cardapio['entrada']:
        print("-", item)
    print("\nPratos Principais:")
    for item in cardapio['prato_principal']:
        print("-", item)
    print("\nSobremesas:")
    for item in cardapio['sobremesa']:
        print("-", item)
    print("\nBebidas:")
    for item in cardapio['bebida']:
        print("-", item)

exibir_cardapio()

# print(cardapio.keys())
# print(cardapio.values())
# chuca = cardapio['entrada']
# print(chuca[0:3])
# rickchivas = chuca.pop(0)
# print(rickchivas)
# print(chuca)