import psycopg2

def conectar_banco():
    try:
        # Substitua pelos seus parâmetros de conexão
        conn = psycopg2.connect(
            host="localhost",
            database="DIDMANAGER",
            user="postgres",
            password="DADOS"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
