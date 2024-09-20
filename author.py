import sqlite3
from database import fetch_query, execute_query
import click 


def create_user(name, email, password):
    """Create a new user"""
    
    insert_query = """
    INSERT INTO users (name, email, password)
    VALUES (?, ?, ?)
    """
    try:
        execute_query(insert_query, (name, email, password))
        return True
    except sqlite3. Error as e:
        print("An error occured while creating the user:", e)
        return False
    

def login_user():
    """ Login user function"""
    global current_user
    email = click.prompt('Enter email')
    password = click.prompt('Enter  password', hide_input=True)
    
    print(f"Fetching user with email: {email} and password: {password}") 
     
    query = "SELECT * FROM user  WHERE email = ? AND password = ?"
    user = fetch_query(query, (email, password))
    
    if user:
        user = user[0]
        click.echo(f'Welcome {user[1]}!')
    else:
        click.echo('Invalid email or password')
        return None
    
    
def view_profile(user_id):
    """ View user profile function"""
    query = "SELECT * FROM user WHERE id = ?"
    user = fetch_query(query, (user_id,))
    
    if user:
        user = user[0]
        click.echo(f'Profile for {user[1]}:')
        click.echo(f"Email:{user[2]}")
        click.echo(f"Admin:{'Yes'if user[4] else 'No'}")
    else:
        click.echo('User not found')