class Book:
    def __init__(self, title, author, genre, release_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.release_year = release_year

# Example database of books
books_db = [
    Book("Book1", "Author A", "Genre X", 2001),
    Book("Book2", "Author B", "Genre Y", 2005),
    Book("Book3", "Author A", "Genre Y", 2005),
    Book("Book4", "Author A", "Genre X", 2005),
]

def find_closest_title(guess_title):
    # Simple implementation of predictive search
    closest_title = None
    shortest_distance = float('inf')
    for book in books_db:
        distance = len(set(guess_title.lower()) ^ set(book.title.lower()))
        if distance < shortest_distance:
            shortest_distance = distance
            closest_title = book.title
    return closest_title

def guess_book(guess_title):
    feedback = {"author": False, "genre": False, "release_year": False}
    guessed_book = next((book for book in books_db if book.title.lower() == guess_title.lower()), None)
    
    if guessed_book:
        feedback["author"] = guessed_book.author == target_book.author
        feedback["genre"] = guessed_book.genre == target_book.genre
        feedback["release_year"] = guessed_book.release_year == target_book.release_year
        return True, feedback
    else:
        # If not found, suggest the closest book title
        closest_title = find_closest_title(guess_title)
        return False, closest_title

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
target_book = Book("Book1", "Author A", "Genre X", 2001)

start_game()
