import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create books table
cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
)
""")

# Clear existing data
cur.execute("DELETE FROM books")

# Insert 8 books
books = [
    (1, "Data Science Basics", "Technology", 1450, 10),
    (2, "Clean Code", "Technology", 1200, 8),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Crash Course", "Technology", 950, 6),
    (5, "The Alchemist", "Fiction", 800, 3),
    (6, "Atomic Habits", "Self-Help", 1100, 7),
    (7, "1984", "Fiction", 900, 10),
    (8, "Deep Work", "Self-Help", 1050, 4)
]

cur.executemany("""
INSERT INTO books
(book_id, title, genre, price, stock)
VALUES (?, ?, ?, ?, ?)
""", books)

conn.commit()

# A. Books with price > 1000
print("Books above Rs.1000 (sorted):")

cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")

for row in cur.fetchall():
    print(row)

# B. Using AS alias
print("\nBook titles with alias:")

cur.execute("""
SELECT title AS book_title, price
FROM books;
""")

for row in cur.fetchall():
    print(row)

# C. Fiction books with stock < 5
print("\nLow-stock Fiction books:")

cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5;
""")

for row in cur.fetchall():
    print(row)

conn.close()