# Função que vai interagir com o Banco de dados


# Criando a tabela
def criarTabela():
    comandos.execute(
        'CREATE TABLE IF NOT EXISTS produtos (titulo text, preco text)')


def InserindoDados(Titulo, Preco):
    comandos.execute("INSERT INTO produtos VALUES(Titulo, Preco)")

    connection.commit()


def CriarDb():
    connection = sqlite3.connect('varredura.db')

    comandos = connection.cursor()
