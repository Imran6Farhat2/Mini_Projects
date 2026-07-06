


import csv
import os

FILE = "books.csv"

# Add Book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author])

    print("Book added successfully!")

# View Books
def view_books():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            print("\nBook List")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Book file not found!")

# Search Book
def search_book():
    book_id = input("Enter Book ID to search: ")
    found = False

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == book_id:
                    print("Book Found:", row)
                    found = True
                    break

        if not found:
            print("Book not found!")

    except FileNotFoundError:
        print("Book file not found!")

# Remove Book
def remove_book():
    book_id = input("Enter Book ID to remove: ")

    try:
        rows = []

        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != book_id:
                    rows.append(row)

        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Book removed successfully!")

    except FileNotFoundError:
        print("Book file not found!")

# Main Menu
while True:
    print("\nLibrary Book Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
