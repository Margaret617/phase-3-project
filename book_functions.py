from database import execute_query, fetch_query
import click


def browse_books():
    """Browser books by category or genre."""
    category = click.prompt('Enter category to browse (Fiction, Non_fiction)', 
                            default=None)
    genre = click.prompt('Enter genre to browse (Fantasy,Sci-Fi)',
                         default=None)
    
    query = "SELECT * FROM books WHERE 1=1"
    params = []
    
    if category:
        query += " AND category = ?"
        params.append(category)
    if genre:
        query += " AND genre = ?"
        params.append(genre)
        
    books = fetch_query(query, params)
    
    if books:
        click.echo('Books:')
        for book in books:
            click.echo(f'ID: {book[0]}, Title: {book[1]}, Author: {book[2]}')
        else:
            click.echo('No books found.')
            
            
def add_book():
    """ Add a new book to the database."""
    title = click.prompt('Enter book title')
    author = click.prompt('Enter book author')
    category = click.prompt('Enter book category eg.FIction,Non-fiction')
    genre = click.prompt('Enter genre eg.Fantasy, Sci-Fi')
    
    query = """ 
    INSERT INTO books (title, author,  category, genre)
    VALUES (?, ?, ?, ?)
    """
    
    params = (title, author, category, genre)
    execute_query(query, params)
    
    click.echo(f'Book "{title}" added successfully!')
    
    
def submit_review(user_id):
    """ Submit a review for a book."""
    book_id = click.prompt('Enter book ID to submit review', type=int)
    rating = click.prompt('Enter rating (1-5)', type=int)
    comment = click.prompt('Enter your review')
    
    query = """
    INSERT INTO reviews (book_id, user_id, rating, comment)
    VALUES  (?, ?, ?, ?)
    """
    
    params = (book_id, user_id, rating, comment)
    execute_query(query, params)
    
    click.echo('Review  submitted successfully!')
    
    
def view_reviews_by_book():
    """  View reviews for a book."""
    book_id = click.prompt('Enter the book ID to view reviews', type=int)
    
    query = "SELECT *  FROM reviews WHERE book_id = ?"
    reviews = fetch_query(query, (book_id))
    
    if reviews:
        click.echo(f'Reviews for Book ID {book_id}:')
        for review in reviews:
            click.echo(f'User ID: {review[2]}, Rating:{review[3]}/ 5,Comment: {review[4]}')
        else:
            click.echo('No reviews found for this book.')
    