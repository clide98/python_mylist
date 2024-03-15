# Task 1: Sum of integers in a list
def sum_of_integers():
    numbers = input("Enter integers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  # Convert input strings to integers
    total_sum = sum(numbers)
    print("Sum of the integers:", total_sum)

# Task 2: Printing favorite books from a tuple
def print_favorite_books():
    favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
    print("My Favorite Books:")
    for book in favorite_books:
        print(book)

# Task 3: Storing person information in a dictionary
def store_person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    print("Person information:", person)

# Task 4: Finding common elements in two sets
def find_common_elements():
    set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
    set2 = set(input("Enter integers for set 2 separated by spaces: ").split())
    common_elements = set1.intersection(set2)
    print("Common elements:", common_elements)

# Task 5: List comprehension to filter words with odd number of characters
def filter_words():
    word_list = input("Enter words separated by spaces: ").split()
    odd_length_words = [word for word in word_list if len(word) % 2 != 0]
    print("Words with odd number of characters:", odd_length_words)

# Main function to execute tasks
if __name__ == "__main__":
    sum_of_integers()
    print()
    print_favorite_books()
    print()
    store_person_info()
    print()
    find_common_elements()
    print()
    filter_words()