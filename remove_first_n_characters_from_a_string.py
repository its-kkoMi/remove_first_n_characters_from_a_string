# Assignment 5 - Exercise 4
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Ask user for input (word and number)

word = str(input("Enter a word: "))
number_of_characters = int(input(f"Enter a number from 0 to {len(word)}: "))

# Remove character using def

def remove_characters(word, number_of_characters):
    print('\nNew String:\n')
    new_string = word[number_of_characters:]
    return new_string

# Print new string

print(remove_characters(word, number_of_characters))