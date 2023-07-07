class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def exibir_produtos(self):
        if len(self.produtos) == 0:
            print("O carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"Nome: {produto.nome}, Preço: R${produto.preco}")

carrinho = CarrinhoDeCompras()

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    preco = float(input("Digite o valor do produto: "))
    produto = Produto(nome, preco)
    carrinho.adicionar_produto(produto)

carrinho.exibir_produtos()

valor_total = carrinho.calcular_valor_total()
print(f"Valor total da compra: R${valor_total}")