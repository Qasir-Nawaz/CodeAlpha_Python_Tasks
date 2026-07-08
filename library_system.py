import sqlite3

# Database Setup
def init_db():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, total_copies INTEGER, available_copies INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS members (member_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, member_id INTEGER, book_id INTEGER, status TEXT)")
    conn.commit()
    conn.close()

class LibrarySystem:
    def add_book(self, title, author, copies):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)", (title, author, copies, copies))
        conn.commit()
        conn.close()
        print("Book added successfully!")

    def view_dashboard(self):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM books")
        print(f"Total Books: {cur.fetchone()[0]}")
        conn.close()

def main():
    init_db()
    lib = LibrarySystem()
    while True:
        print("\n--- Library System Menu ---")
        print("1. Add Book\n2. View Dashboard\n3. Exit")
        choice = input("Select option: ")
        if choice == '1':
            lib.add_book(input("Title: "), input("Author: "), int(input("Copies: ")))
        elif choice == '2':
            lib.view_dashboard()
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
