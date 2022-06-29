
from __future__ import print_function

words = []
colors = ["g", "y", "w"]


with open('words.txt') as f:
    for word in f:
        words.append(word.strip())

initialWordlist = set(words)

for i in range(6):
    while True:
        count = 0
        guess = input("Word guess: ").lower()
        if len(guess) != 5:
            print("please input 5 letter guess")
            continue

        if guess not in initialWordlist:
            print("not a valid word, please try again")
            continue

        print("Color of tiles: g - green/correct letter, y - yellow, w - wrong/grey")

        feedback = input("Feedback: ").lower()
        if len(feedback) != 5:
            print("please provide 5 letters for feedback (g/y/w)")
            continue
        for element in feedback:
            if element not in colors:
                print("please be sure to type g, y, or w for feedback")
                counte = 1
                break
        if count == 1:
            continue
        greys = []
        greens = []
        yellows = []
        for i in range(5):
            if feedback[i] == "w":
                greys.append(guess[i])
            elif feedback[i] == "g":
                greens.append(guess[i])
            else:
                yellows.append(guess[i])

        if bool(set(greys) & set(yellows)) == True:
            print("Error: cannot have a letter be in green and grey at the same time")
            print("If a letter appears more than one time- and one of those tiles is green or yellow")
            print("while the other tile is grey- please enter the grey tile as yellow")
            print("please try again")
            continue
        if bool(set(greys) & set(greens)) == True:
            print("Error: cannot have a letter be in green and grey at the same time")
            print("If a letter appears more than one time- and one of those tiles is green or yellow")
            print("while the other tile is grey- please enter the grey tile as yellow")
            print("please try again")
            continue
        break

    if feedback == "ggggg":
        print("nice! you wont the big game and you only had to use this stupid program to help")
        print("maybe try expanding your vocab a little, idiot")
        break

    word_tuple = tuple(words)

    for word in word_tuple:
        for i in range(5):
            if feedback[i] == "g" and guess[i] != word[i]:
                words.remove(word)
                break
            elif feedback[i] == "w" and guess[i] in word:
                words.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                words.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                words.remove(word)
                break
    print("possible remaining words")
    counter = 0
    for word in words:
        print(word, end = ", ")
        counter += 1
        if counter == 8:
            print("")
            counter = 0
    print("")