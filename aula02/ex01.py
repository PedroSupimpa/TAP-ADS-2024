class Salario:
    def __init__(self, id_salario, valor):
        self.id_salario = id_salario
        self.valor = valor

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.salario = None 

    def set_salario(self, salario):
        self.salario = salario

class Cliente:
    def __init__(self, id_cliente, nome, endereco):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

class Venda:
    def __init__(self, id_venda, data):
        self.id_venda = id_venda
        self.data = data
        self.vendedor = None  
        self.comprador = None  
        self.itens_vendidos = []  
    def adicionar_item(self, produto, quantidade):
        self.itens_vendidos.append({"produto": produto, "quantidade": quantidade})

    def calcular_total(self):
        total = 0
        for item in self.itens_vendidos:
            total += item["produto"].preco * item["quantidade"]
        return total


salario_john = Salario(1, 50000)
john = Funcionario(1, "John Doe", "Vendedor")
john.set_salario(salario_john)

cliente_maria = Cliente(1, "Maria Silva", "Rua ABC, 123")
produto_laptop = Produto(1, "Laptop", 2000)

venda1 = Venda(1, "2024-03-06")
venda1.vendedor = john
venda1.comprador = cliente_maria
venda1.adicionar_item(produto_laptop, 2)

print(f"Total da venda: R${venda1.calcular_total()}")
