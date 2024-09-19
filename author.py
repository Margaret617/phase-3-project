from database import fetch_query, execute_query
import click 


def login_user():
    """ Login user function"""
    email = click.prompt('Enter email')
    password = click.prompt('Enter  password', hide_input=True)
    
    query = "SELECT * FROM user  WHERE email = ? AND password = ?"
    user = fetch_query(query, (email, password))
    
    if user:
        user = user[0]
        click.echo(f'Welcome {user[1]}!')
        return user
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