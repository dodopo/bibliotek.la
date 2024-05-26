#minha_biblioteca_json
import subprocess
import json


class Book:
    def __init__(self, title, author, genre, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["genre"], data["quantity"])


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def delete_book(self, criterion, value):
        results = self.search_book(criterion, value)
        if results:
            print("Found the following books:")
            self.print_books(results)
            delete_choice = input("Enter the index(es) of the book(s) to delete (separated by comma): ")
            indexes = [int(index.strip()) - 1 for index in delete_choice.split(",") if index.strip()]
            for index in sorted(indexes, reverse=True):
                if 0 <= index < len(results):
                    book_to_delete = results[index]
                    self.books.remove(book_to_delete)
            self.save_books()
            print("Book(s) deleted successfully.")
        else:
            print(f"No books found with '{value}' in {criterion}.")

    def edit_book(self, book):
        print("Select the criteria you want to edit:")
        print("1. Title")
        print("2. Author")
        print("3. Genre")
        print("4. Quantity")
        edit_choice = int(input("Enter your choice: "))

        if edit_choice == 1:
            new_title = input("Enter the new title: ")
            book.title = new_title
        elif edit_choice == 2:
            new_author = input("Enter the new author: ")
            book.author = new_author
        elif edit_choice == 3:
            new_genre = input("Enter the new genre: ")
            book.genre = new_genre
        elif edit_choice == 4:
            new_quantity = int(input("Enter the new quantity: "))
            book.quantity = new_quantity
        else:
            print("Invalid choice.")
            return

        self.save_books()
        print("Book edited successfully.")

    def search_book(self, criterion, value):
        results = []
        for book in self.books:
            if value.lower() in getattr(book, criterion).lower():
                results.append(book)
        return results

    def print_books(self, books):
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")

    def save_books(self):
        with open('books.json', 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def load_books(self):
        try:
            with open('books.json', 'r', encoding='utf-8') as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(book_data) for book_data in books_data]
        except FileNotFoundError:
            self.books = []


def main():
    library = Library()

    while True:
        print("\n1. Add a book")
        print("2. Delete a book")
        print("3. Edit a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Clear screen")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            quantity = int(input("Enter book quantity: "))
            library.add_book(Book(title, author, genre, quantity))
        elif choice == 2:
            print("Search by:\n1. Title\n2. Author\n3. Genre")
            search_choice = int(input("Enter your choice: "))
            if search_choice == 1:
                criterion = "title"
            elif search_choice == 2:
                criterion = "author"
            elif search_choice == 3:
                criterion = "genre"
            else:
                print("Invalid choice. Please try again.")
                continue
            value = input(f"Enter part of the {criterion}: ")
            library.delete_book(criterion, value)
        elif choice == 3:
            print("Search by:\n1. Title\n2. Author\n3. Genre")
            search_choice = int(input("Enter your choice: "))
            if search_choice == 1:
                criterion = "title"
            elif search_choice == 2:
                criterion = "author"
            elif search_choice == 3:
                criterion = "genre"
            else:
                print("Invalid choice. Please try again.")
                continue
            value = input(f"Enter part of the {criterion}: ")
            results = library.search_book(criterion, value)
            if results:
                library.print_books(results)
                book_index = int(input("Enter the index of the book to edit: ")) - 1
                if 0 <= book_index < len(results):
                    library.edit_book(results[book_index])
                else:
                    print("Invalid book index.")
            else:
                print("No books found.")
        elif choice == 4:
            print("Search by:\n1. Title\n2. Author\n3. Genre")
            search_choice = int(input("Enter your choice: "))
            if search_choice == 1:
                criterion = "title"
            elif search_choice == 2:
                criterion = "author"
            elif search_choice == 3:
                criterion = "genre"
            else:
                print("Invalid choice. Please try again.")
                continue
            value = input(f"Enter part of the {criterion}: ")
            results = library.search_book(criterion, value)
            if results:
                library.print_books(results)
            else:
                print("No books found.")
        elif choice == 5:
            library.print_books(library.books)
        elif choice == 6:
            subprocess.run(['clear'])
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
