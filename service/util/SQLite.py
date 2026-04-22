import sqlite3

from typing import List, Optional, Union

DB_PATH = "Chat.db"

# ===========================
# Funções utilitárias de DB
# ===========================

def _get_conn():
    """Abre conexão com SQLite e retorna com row_factory configurado"""
    conn = sqlite3.connect(
        DB_PATH,
        timeout=10, 
        check_same_thread=False 
    )
    
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA journal_mode=WAL;")  
    return conn

# ---------------------------
# SELECT múltiplos resultados
# ---------------------------
def query(sql: str, params: tuple = ()) -> List[dict]:
    """
    Executa SELECT e retorna lista de dicionários.
    """
    conn = _get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ---------------------------
# SELECT único resultado
# ---------------------------
def one(sql: str, params: tuple = ()) -> Optional[dict]:
    """
    Executa SELECT e retorna um único registro como dicionário.
    Retorna None se não existir.
    """
    conn = _get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

# ---------------------------
# INSERT / UPDATE / DELETE
# ---------------------------
def execute(sql: str, params: tuple = ()) -> int:
    """
    Executa INSERT, UPDATE ou DELETE.
    Retorna lastrowid (ID do último registro inserido) para INSERT.
    """
    conn = _get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

# ---------------------------
# Exemplo de uso rápido:
# ---------------------------
if __name__ == "__main__":
    # Listar todos os perfis
    perfis = query("SELECT * FROM profiles")
    print("Todos os perfis:", perfis)

    # Buscar 1 perfil
    perfil = one("SELECT * FROM profiles WHERE user_id = ?", (1,))
    print("Perfil 1:", perfil)

    # Inserir novo perfil
    novo_id = execute(
        "INSERT INTO profiles (name, status) VALUES (?,?)",
        ("Guilherme", "online")
    )
    print("Novo perfil criado com ID:", novo_id)

    # Atualizar perfil
    execute(
        "UPDATE profiles SET status = ? WHERE user_id = ?",
        ("offline", 1)
    )
    print("Perfil atualizado")