# Book Review System

A command-line interface (CLI) application for managing a book review system. Users can create accounts, browse books, submit reviews, and view reviews by book.

## Features

- User registration and login
- Browse books by category and genre
- Submit and view reviews for books
- Admin functionalities (if implemented)

## Technologies Used

- Python 3
- SQLite for the database
- Click for command-line interface

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Step-by-Step Installation

1. Clone the repository:
   git clone `git@github.com:Margaret617/phase-3-project.git`

2. Create a virtual environment (optional but recommended):
python3 -m venv myenv
source myenv/bin/activate

3. Install required packages:
pip install -r requirements.txt
pip install click
pip install sqlite3

4. Initialize the database:
python3 cli.py init

## Usage
### Commands
- Create a new user:
python3 cli.py create_user_command [email] [password]

- Login to the system:
python3 cli.py login

- Browse books:
python3 cli.py browse

- Submit a review:
python3 cli.py submit_review_command

- View reviews for a specific book:
python3 cli.py view_reviews

- View user profile:
python3 cli.py profile

## Database Schema
The application uses a SQLite database with the following tables:

- users

id (INTEGER, PRIMARY KEY)
name (TEXT)
email (TEXT, UNIQUE)
password (TEXT)
is_admin (BOOLEAN)
- books

id (INTEGER, PRIMARY KEY)
title (TEXT)
author (TEXT)
category (TEXT)
genre (TEXT)
- reviews

id (INTEGER, PRIMARY KEY)
user_id (INTEGER, FOREIGN KEY)
book_id (INTEGER, FOREIGN KEY)
rating (INTEGER)
comment (TEXT)
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
