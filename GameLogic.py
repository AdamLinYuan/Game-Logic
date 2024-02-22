class Book:
    def __init__(self, title, author, genre, release_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.release_year = release_year

# Example database of books
books_db = [
    Book("Book1", "Author A", "Genre X", 2001),
    Book("Book2", "Author B", "Genre Y", 2005), # No Matching properties
    Book("Book3", "Author A", "Genre Y", 2005), # 1 Matching property
    Book("Book4", "Author A", "Genre X", 2005), # 2Book Matching properties
    # Add more books as needed
]

# Target book for the user to guess
target_book = Book("Book Title 1", "Author A", "Genre X", 2001)

def guess_book(guess_title):
    feedback = {"author": False, "genre": False, "release_year": False}
    guessed_book = next((book for book in books_db if book.title.lower() == guess_title.lower()), None)
    
    if guessed_book:
        feedback["author"] = guessed_book.author == target_book.author
        feedback["genre"] = guessed_book.genre == target_book.genre
        feedback["release_year"] = guessed_book.release_year == target_book.release_year
        return True, feedback
    else:
        return False, None

def start_game():
    max_guesses = 3
    guess_count = 0
    
    while guess_count < max_guesses:
        user_guess = input("Guess the book title: ")
        found, feedback = guess_book(user_guess)
        
        if not found:
            print("The book is not in our database, try again.")
            continue
        
        guess_count += 1
        if all(feedback.values()):
            print(f"Congratulations! You've guessed the book correctly in {guess_count} {'guess' if guess_count == 1 else 'guesses'}.")
            break
        else:
            print("Feedback on your guess:", feedback)
        
        if guess_count == max_guesses:
            print(f"Sorry, you've reached the maximum number of guesses. The correct book was '{target_book.title}'.")

start_game()
