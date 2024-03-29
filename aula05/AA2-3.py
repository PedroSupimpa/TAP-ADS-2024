class Retangulo:
    def __init__(self, largura=0, altura=0):
        self.largura = largura
        self.altura = altura
        self.nome = ""

    def get_largura(self):
        return self.largura

    def set_largura(self, largura):
        self.largura = largura

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_area(self):
        return self.largura * self.altura


class Impressao:
    def imprimir(retangulo: Retangulo):
        print("Retângulo:")
        print(f"Largura: {retangulo.get_largura()}")
        print(f"Altura: {retangulo.get_altura()}")
        print(f"Área: {retangulo.get_area()}")


class Salvamento:
    def salvar_em_arquivo(retangulo: Retangulo, nome_arquivo="retangulo.txt"):
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(f"Largura: {retangulo.get_largura()}\n")
            arquivo.write(f"Altura: {retangulo.get_altura()}\n")
            arquivo.write(f"Área: {retangulo.get_area()}\n")



retangulo = Retangulo(10, 20)
Impressao.imprimir(retangulo)
Salvamento.salvar_em_arquivo(retangulo)
