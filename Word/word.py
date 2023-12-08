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
    answer = list(answer)
    result = [None] * len(answer)
    # Greens
    for i in range(len(answer) - 1, -1, -1):
        if guess[i] == answer[i]:
            result[i] = [guess[i].upper(), Fore.GREEN]
            answer.pop(i)

    # Yellows
    for i in range(len(answer) - 1, -1, -1):
        if guess[i] in answer:
            result[i] = [guess[i].upper(), Fore.YELLOW]
            answer.pop(answer.index(guess[i]))

    # Whites
    for i in range(len(result) - 1, -1, -1):
        if result[i] == None:
            result[i] = [guess[i].upper(), Fore.WHITE]

    return result

def list_to_string(list):
    string = '|'
    for i in range(len(list)):
        if i == int(len(list)/2):
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
        elif letters[i][0] in yellows and letters[i][0] != Fore.GREEN:
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
        letters = [['A', Fore.WHITE], ['B', Fore.WHITE], ['C', Fore.WHITE], ['D', Fore.WHITE], ['E', Fore.WHITE], ['F', Fore.WHITE], ['G', Fore.WHITE], ['H', Fore.WHITE], ['I', Fore.WHITE], ['J', Fore.WHITE], ['K', Fore.WHITE], ['L', Fore.WHITE], ['M', Fore.WHITE], ['N', Fore.WHITE], ['O', Fore.WHITE], ['P', Fore.WHITE], ['Q', Fore.WHITE], ['R', Fore.WHITE], ['S', Fore.WHITE], ['T', Fore.WHITE], ['U', Fore.WHITE], ['V', Fore.WHITE], ['W', Fore.WHITE], ['X', Fore.WHITE], ['Y', Fore.WHITE], ['Z', Fore.WHITE]]
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
            if len(guess) != 5 or guess not in self.words:
                valid = False
            
            if valid:
                checked = check_word(guess, self.word)
                letters = update_letters(letters, checked)
                guesses[guess_count] = checked
                guess_count += 1
        clear_screen()
        print_list(guesses)
        print(f'WORD WAS: {self.word.upper()}')