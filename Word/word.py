import random
from colorama import Fore
import sys
from os import system

def clear_screen():
    if sys.platform.startswith('win'):
        system('cls')
    else:
        system('clear')

def read_file(file_name):
    with open(file_name) as file:
        lst = file.readlines()
        
        for i in range(0, len(lst)):
            lst[i] = lst[i].strip()

    return lst

def print_word(word, message=None):
    for set in word:
        print(f'{set[1]}[{set[0]}]{Fore.RESET}', end='')
    if message:
        print(f' {message}')
    else:
        print(' ')

def print_list(list, message):
    if message:
        message = message.split('\n')
    for i in range(len(list)):
        try:
            print_word(list[i], message[i])
        except:
            print_word(list[i])

def check_word(guess, answer):
    ret = [None] * 5
    compare = list(answer)

    # Greens
    for i in range(len(guess)):
        if guess[i] == compare[i]:
            ret[i] = [guess[i].upper(), Fore.GREEN]
            compare[i] = None

    # Yellows
    for i in range(len(guess)):
        if guess[i] in compare:
            ret[i] = [guess[i].upper(), Fore.YELLOW]
            compare[compare.index(guess[i])] = None

    # Whites
    for i in range(len(ret)):
        if ret[i] == None:
            ret[i] = [guess[i].upper(), Fore.WHITE]

    return ret

def list_to_string(list):
    string = '|'
    for i in range(len(list)):
        if list[i][0] in ['A', 'Z']:
            string += '\n|'
        string += (list[i][1]+list[i][0]+Fore.RESET+'|')
    return string

def update_letters(letters, checked):
    greens = []
    reds = []
    yellows = []

    for i in range(len(checked)):
        if checked[i][1] == Fore.GREEN:
            greens.append(checked[i][0])
        elif checked[i][1] == Fore.YELLOW:
            yellows.append(checked[i][0])
        elif checked[i][1] == Fore.WHITE:
            reds.append(checked[i][0])
    
    for i in range(len(letters)):
        if letters[i][0] in greens:
            letters[i][1] = Fore.GREEN
        elif letters[i][0] not in greens and letters[i][1] != Fore.GREEN and letters[i][0] in yellows:
            letters[i][1] = Fore.YELLOW
        elif letters[i][0] in reds and letters[i][0] not in [Fore.GREEN, Fore.YELLOW]:
            letters[i][1] = Fore.RED

    return letters



class Word:
    def __init__(self):
        self.words = read_file('Word/words.txt')

    def play(self, word=None):
        # Play with custom word
        if word:
            self.word = word
        else:
            self.word = random.choice(self.words)
        
        # Initialize variables
        letters = [['Q', Fore.WHITE], ['W', Fore.WHITE], ['E', Fore.WHITE], ['R', Fore.WHITE], ['T', Fore.WHITE], ['Y', Fore.WHITE], ['U', Fore.WHITE], ['I', Fore.WHITE], ['O', Fore.WHITE], ['P', Fore.WHITE], ['A', Fore.WHITE], ['S', Fore.WHITE], ['D', Fore.WHITE], ['F', Fore.WHITE], ['G', Fore.WHITE], ['H', Fore.WHITE], ['J', Fore.WHITE], ['K', Fore.WHITE], ['L', Fore.WHITE], ['Z', Fore.WHITE], ['X', Fore.WHITE], ['C', Fore.WHITE], ['V', Fore.WHITE], ['B', Fore.WHITE], ['N', Fore.WHITE], ['M', Fore.WHITE]]
        guess_count = 0
        guess = ' '
        guesses = [[[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]], [[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]], [[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]], [[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]], [[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]], [[' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE], [' ', Fore.WHITE]]]

        # Gives user 6 guesses
        while guess_count < 6 and self.word != guess:
            clear_screen()
            print_list(guesses, list_to_string(letters))

            guess = input().lower()

            # Check for validity
            valid = True
            if guess == 'exit':
                clear_screen()
                exit()
                
            if len(guess) != 5 or guess not in self.words:
                valid = False
            
            if valid:
                checked = check_word(guess, self.word)
                letters = update_letters(letters, checked)
                guesses[guess_count] = checked
                guess_count += 1
        clear_screen()
        print_list(guesses, list_to_string(letters))
        print(f'WORD WAS: {self.word.upper()}')
        input('Press Enter to Play Again . . .')

        self.play()