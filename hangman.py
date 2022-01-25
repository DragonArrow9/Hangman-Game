import random

word_bank = ["apple", "banana", "carrot"]
word = random.choice(word_bank)
unknown_word = []
guesses = 6
letters_guessed = []

for letter in word:
    unknown_word += "-"

print("".join(unknown_word))

while True:
    user_input = input("Enter a letter: ")
    letters_guessed += user_input
    count = 0
    correct_letter = False

    if word.__contains__(user_input):
        correct_letter = True
    
    for letter in word:
        if letter == user_input:
            unknown_word[count] = letter
        count += 1

    if correct_letter == False:
        guesses -= 1

    if guesses < 1:
        print("You lose.")
        break
    
    if unknown_word.count("-") == 0:
        print("You win!")
        break
    
    print("".join(unknown_word))
    print("Guessed Letters: %s" % ", ".join(letters_guessed)) 
    print("You have %s remaining guesses." % guesses)
    print("")

input("Press 'Enter' to exit.")

    