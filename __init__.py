from database import execute_query


def init_db():
    """Initialize the database by creating the necessary tables."""
    execute_query("""
                  CREATE TABLE IF NOT EXISTS users(
                      id INTEGER PRIMARY KEY  AUTOINCREMENT,
                      name TEXT NOT NULL,
                      email  TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL,
                      is_admin  INTEGER NOT NULL DEFAULT 0
                      )
                      """
                  )
     
    execute_query("""
                  CREATE TABLE IF NOT EXISTS books(
                      id INTEGER PRIMARY  KEY  AUTOINCREMENT,
                      title  TEXT NOT NULL,
                      author TEXT NOT NULL,
                      category  TEXT NOT NULL,
                      genre TEXT NOT NULL
                      )
                      """)
    
    execute_query("""
                  CREATE TABLE IF NOT EXISTS reviews(
                      id  INTEGER PRIMARY KEY AUTOINCREMENT,
                      book_id INTEGER NOT NULL,
                      user_id INTEGER NOT NULL,
                      rating INTEGER NOT NULL,
                      comment  TEXT NOT NULL,
                      FOREIGN KEY (book_id) REFERENCES books(id),
                      FOREIGN  KEY (user_id) REFERENCES users(id)
                      )
                      """
                  )
    
    
if __name__ == '__main__':
    init_db()
    print("Database initialized.")