import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Define a base class for models
class Base(DeclarativeBase):
    pass

# Initialize the SQLAlchemy object
db = SQLAlchemy(model_class=Base)

# Create the Flask app
app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the extension
db.init_app(app)

# Define a model (table) class for Books
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Delete the old database file if it exists
if os.path.exists("project.db"):
    os.remove("project.db")

# Create the database and tables
with app.app_context():
    db.create_all()

# Add a new book to the database
with app.app_context():
    # Check if the book already exists
    existing_book = Book.query.filter_by(title="Harry Potter").first()
    if not existing_book:
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)