import random
from words import guess_word_list, valid_word_list

print("=== W O R D L E ===")
print(f"Cached {len(guess_word_list)} words.")
mode = int(input("Select a mode, Enter (1) for Debug Mode, (2) for Test Mode: "))
word_comp = 0
guessed_word_list = []
green_list = []
guessing_count = 0
word_aimed = ""
break_out_flag = False
if mode == 1:
    word_comp = int(input("Enter an index in between 0-548: "))
    print(f"The selected word is: {guess_word_list[word_comp]}")
    word_aimed = guess_word_list[word_comp]
if mode == 2:
    word_comp = random.randint(0, len(guess_word_list))
    print(f"The selected word is: {guess_word_list[word_comp]}")
    word_aimed = guess_word_list[word_comp]



def is_valid(word):
    if len(word) != 5:
        print("Word length should be 5.")
        return False
    elif not word in valid_word_list:
        print(f"Word {word} is not found in the list.")
        return False
    else:
        return True





while guessing_count <= 4:
    word_user = input("Enter a word: ")
    if is_valid(word_user):
        guessed_word_list.append(word_user)
        for t in range(guessing_count+1):
            if guessed_word_list[t] == word_aimed:
                for char in guessed_word_list[t]:
                    print(char.upper(), end=" ")
                    break_out_flag = True
                print("")
                break
            for j in range(len(guessed_word_list[t])):
                if guessed_word_list[t][j] == word_aimed[j]:
                    print(f"\033[92m{guessed_word_list[t][j]}\033[0m", end=" ")
                    green_list.append(guessed_word_list[t][j])
                elif (guessed_word_list[t][j] in word_aimed) and (guessed_word_list[t].count(guessed_word_list[t][j]) - word_aimed.count(guessed_word_list[t][j])) <= 0:
                    print(f"\033[1;33m{guessed_word_list[t][j]}\033[0m", end=" ")
                else:
                    print(guessed_word_list[t][j], end=" ")
            green_list = []

            print("")
        print("- - - - - \n"*(4-guessing_count), end=" ")
        print("")
        guessing_count += 1
        if break_out_flag == True:
            break


