import sqlite3

DATABASE = "books.db"


def get_connection():
    ''' get a new connection to the database.'''
    conn = sqlite3.connect(DATABASE)
    return conn


def execute_query(query, params=()):
    ''' execute a query on the database and return the results'''
    print("Executing query:", query)
    print("With params:", params)
    with get_connection() as conn:
        Cursor = conn.cursor()
        Cursor.execute(query, params)
        conn.commit()
        
        
def fetch_query(query, params=()):
    ''' execute a query on the database and return the results'''
    print("Fetching query:", query)
    print("With params:", params)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    

