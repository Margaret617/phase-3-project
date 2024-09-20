import click
from book_functions import browse_books, submit_review, view_reviews_by_book, add_book
from author import login_user, view_profile, create_user
from database import init_db

current_user = None


@click.group()
def cli():
    """ Main CLI group """
    pass


@click.command(name='create_user_command')
@click.argument('email')
@click.argument('password')
def create_user_command(email, password):
    """  Create a new user """
    name = click.prompt("Enter your name")
    if create_user(name, email, password):
        click.echo(f'user "{name}" created successfully with email"{email}"!')
    else:
        click.echo('Failed to create user.')
    
    
cli.add_command(create_user_command)


@cli.command()
def init():
    """ Initialize the database """
    init_db()
    click.echo('Database initialized.')
    
    
@cli.command()
def login():
    """ Login to the system """
    user = login_user()
    if user:
        click.echo(f'Logged in as {user[1]}')
        
        
@cli.command()
def add_book_command():
    """ Add a book """
    add_book()
    
    
@cli.command()
def browse():
    """ Browse books """
    browse_books()
    
    
@cli.command()
def submit_review_command():
    """ Submit  a review  """
    user = login_user()
    if user:
        submit_review(user[0])
        
        
@cli.command()
def view_reviews():
    """ View reviews for a book """
    view_reviews_by_book()
    
    
@cli.command()
def profile():
    """ View user profile """
    user = login_user()
    if user:
        view_profile(user[0])
        

if __name__ == '__main__':
    cli()