from flask import Flask, render_template, request, redirect, url_for
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


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db.init_app(app)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

if os.path.exists("project.db"):
    os.remove("project.db")

with app.app_context():
    db.create_all()

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    print(all_books)
    return render_template("index.html", books = all_books)

@app.route("/add" , methods=["GET" , "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(id=1, title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/editrating/<int:book_id>", methods=["GET", "POST"])
def editrating(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        new_rating = request.form["rating"]
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("editrating.html", book=book)

@app.route("/delete/<int:book_id>", methods=["POST"])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

