import csv


# exercicio01

def contar_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        linhas = conteudo.split('\n')
        linhas = [linha for linha in linhas if linha.strip() != '']
        return len(linhas)

txtFile = 'exemplotxt.txt'
print(contar_linhas(txtFile))


# exercicio02

def contar_palavras_unicas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        palavras_unicas = set(palavras)
        return len(palavras_unicas)


print(contar_palavras_unicas('txtFile'))


# exercicio03

def calcular_media_produtos(nome_arquivo):
    total_preco = 0
    total_produtos = 0
    with open(nome_arquivo, mode='r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            total_preco += float(linha['preco'])
            total_produtos += 1
    return total_preco / total_produtos if total_produtos else 0



csvFile = 'produtos.csv'
media_precos = calcular_media_produtos(csvFile)

print(media_precos)