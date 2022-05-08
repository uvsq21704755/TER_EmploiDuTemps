from psycopg2 import *
import psycopg2

def connexion():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="moulhat",
            host="localhost",
            port="5432",
            database="EDT"
        )

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à PostgreSQL", error)

    return (conn)

def close_connexion(conn, cur):
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")


