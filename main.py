import random
def get_random_word_from_wordlist():
    wordlist = []
    with open("hangman_wordlist.txt",'r') as file:
        wordlist = file.read().split("\n")
    return random.choice(wordlist)

def get_some_letters(word):
    return '_' * len(word)

def draw_hangman(chances):
   hangman = [
       "____________"
       " |  | "
       " |  0 "
       " |  /|\ "
       " |  / \ "
       " |  "
   ]
   print('\n'.join(hangman[0:7-chances]))

def start_hangman_game():
    name = input("What is your name? ")
    print("Hello, " + name, "Time to play hangman!")

    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    chances = 7
    found = False

    while chances > 0:
        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have:").lower()

        if len(character) != 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
        elif character in temp:
            print("You have already guessed that letter.Try another one.")

        if character in word:
            temp = ''.join([char if char == character or char in temp else '_' for char in word])
            if temp == word:
                print(f"\nYou Won! The word was: {word}")
                print(f"You got it in {7 - chances} guess")
                break
        else:
            chances -= 1
            draw_hangman(chances)
            
    if chances == 0:
        print(f"Sorry, {name}! You lost. The word was: {word}. Better luck next time.")

start_hangman_game()


