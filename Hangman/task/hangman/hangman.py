# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']

def enter_letter(set):
    while True:
        print(''.join(w_list))
        l = input("Input a letter: ")
        if len(l) > 1:
            print("You should input a single letter\n")
            continue
        if l in set:
            print("You've already guessed this letter\n")
            continue
        if l not in "abcdefghijklmnopqrstuvwxyz" or l == " " or len(l) == 0:
            print("Please enter a lowercase English letter\n")
            continue
        return l

def menu():
    while True:
        vopros = input('Type "play" to play the game, "exit" to quit: ')
        if vopros == "play" or vopros == "exit":
            print()
            return vopros



print('H A N G M A N')
print()


flag = "play"

while True:
    word = random.choice(words)
    word_list = list(word)
    w = "-" * len(word)
    w_list = list(w)
    word_ansower = w
    letter_set = set()
    count = 0
    flag = menu()
    if flag == "exit":
        break
    while count < 8:
        letter = enter_letter(letter_set)
        if letter in word_list and letter not in letter_set:
            letter_count = word.count(letter)
            count_index = 0
            letter_set.add(letter)
            while count_index < letter_count:
                letter_index = word_list.index(letter)
                if w_list[letter_index] != letter:
                    w_list[letter_index] = letter
                    word_list[letter_index] = "-"
                    count_index += 1
            word_ansower = ''.join(w_list)
            if word_ansower == word:
                break
        elif letter not in word_list:
            print("That letter doesn't appear in the word")
            letter_set.add(letter)
            count += 1
        if count <= 7:
            print()
    if word == word_ansower:
        print()
        print(word_ansower)
        print("You guessed the word!")
        print("You survived!\n")
    else:
        print("You lost!\n")










