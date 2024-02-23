from difflib import get_close_matches

class Book:
    def __init__(self, title, author, genre, release_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.release_year = release_year

# Example database of books
books_db = [
    Book("To Kill a Mockingbird", "Harper Lee", "Classic", 1960),
    Book("1984", "George Orwell", "Dystopian", 1949),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925),
    Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Magical Realism", 1967),
    Book("Pride and Prejudice", "Jane Austen", "Classic Romance", 1813),
    Book("The Catcher in the Rye", "J.D. Salinger", "Literary Fiction", 1951),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954),
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 1997),
    Book("The Book Thief", "Markus Zusak", "Historical Fiction", 2005),
    Book("The Chronicles of Narnia", "C.S. Lewis", "Fantasy", 1950),
    Book("Animal Farm", "George Orwell", "Dystopian", 1945),
    Book("Brave New World", "Aldous Huxley", "Dystopian", 1932),
    Book("Fahrenheit 451", "Ray Bradbury", "Dystopian", 1953),
    Book("Jane Eyre", "Charlotte Bronte", "Classic Romance", 1847),
    Book("Wuthering Heights", "Emily Bronte", "Classic Romance", 1847),
    Book("The Alchemist", "Paulo Coelho", "Adventure Fiction", 1988),
    Book("Moby Dick", "Herman Melville", "Adventure Fiction", 1851),
    Book("War and Peace", "Leo Tolstoy", "Historical Fiction", 1869),
    Book("The Catch-22", "Joseph Heller", "Satire", 1961),
]

def find_closest_titles(guess_title, num_suggestions=3):
    # Collect all book titles from the database
    all_titles = [book.title for book in books_db]
    # Use get_close_matches to find the closest titles based on the guess
    closest_titles = get_close_matches(guess_title, all_titles, n=num_suggestions, cutoff=0.1)
    return closest_titles

def guess_book(guess_title):
    feedback = {"author": False, "genre": False, "release_year": False}
    guessed_book = next((book for book in books_db if book.title.lower() == guess_title.lower()), None)
    
    if guessed_book:
        feedback["author"] = guessed_book.author == target_book.author
        feedback["genre"] = guessed_book.genre == target_book.genre
        feedback["release_year"] = guessed_book.release_year == target_book.release_year
        return True, feedback
    else:
        # If not found, suggest the closest book titles
        closest_titles = find_closest_titles(guess_title)
        return False, closest_titles
    
def start_game():
    max_guesses = 3
    guess_count = 0
    
    while guess_count < max_guesses:
        user_guess = input("Guess the book title: ")
        found, result = guess_book(user_guess)
        
        if not found:
            print(f"The book is not in our database. Did you mean '{result}'? Try again.")
            continue
        
        guess_count += 1
        if all(result.values()):
            print(f"Congratulations! You've guessed the book correctly in {guess_count} {'guess' if guess_count == 1 else 'guesses'}.")
            break
        else:
            print("Feedback on your guess:", result)
        
        if guess_count == max_guesses:
            print(f"Sorry, you've reached the maximum number of guesses. The correct book was '{target_book.title}'.")

# Define the target book for the game
target_book = books_db[1]

start_game()
