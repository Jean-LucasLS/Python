def print_aligned(items):
    max_product_len = max(len(product) for product, _ in items)
    max_price_len = max(len("{:.2f}".format(price)) for _, price in items)

    print(f"{'Produto':<{max_product_len}} | {'Preço':>{max_price_len}}")
    print("-" * (max_product_len + max_price_len + 5))

    total = 0
    for product, price in items:
        print(f"{product:<{max_product_len}} | {price:>{max_price_len}.2f}")
        total += price

    print("-" * (max_product_len + max_price_len + 5))
    print(f"{'Total':<{max_product_len}} | {total:>{max_price_len}.2f}")

if __name__ == "__main__":
    # Exemplo de lista de produtos e preços
    produtos_precos = [
        ("Cadeira Gamer", 500.00),
        ("Mesa em L", 604.00),
        ("Manutenção do Carro", 434.00),
        ("Suplementos", 230.00),
        ("Curso de Formação em Dados", 640.00)
    ]

    print_aligned(produtos_precos)

import matplotlib.pyplot as plt
    
# Separando os dados para o gráfico
produtos, precos = zip(*produtos_precos)
print(produtos)
print(precos)

# # Criação do gráfico de barras
# plt.bar(produtos, precos)

# # Personalização do gráfico (opcional)
# plt.title('Preços dos Produtos')
# plt.xlabel('Produtos')
# plt.ylabel('Preços (R$)')

# # Rotacionar os rótulos do eixo X para melhor visualização
# plt.xticks(rotation=45, ha='right')

# # Exibição do gráfico
# plt.tight_layout()  # Ajustar layout para evitar sobreposição de rótulos
# plt.show()