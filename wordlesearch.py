# initialize words list and colors list
words = []
colors = ["g", "y", "w"]

# open document of all words list into words variable
try:
    with open('words.txt') as f:
        for word in f:
            words.append(word.strip())
except FileNotFoundError:
    print("Error, cannot open file")

# set initial words list. this will make sure user always inputs valid word
initialWordList = set(words)

# loop thru 5 guesses
for i in range(6):
    # while true makes sure the user inputs a correct word and that the feedback is either g, y, or w
    # if user makes any mistake, the loop will start over and ask for inputs again until it reaches the end and breaks
    while True:
        count = 0
        guess = input("guess word:  ").lower()
        # verifies a 5 letter word
        if len(guess) != 5:
            print("please input 5 letter word")
            continue
        # verifies word is valid (from word text document)
        if guess not in initialWordList:
            print("not a valid word, please try again")
            continue
        print("Color of blocks: g - green/correct letter, y - yellow, w - wrong/grey")
        # asks for the feedback (color of wordle tiles after submitted)
        feedback = input("Feedback: ").lower()
        if len(feedback) != 5:
            print("please provide 5 letters for feedback (g/y/w)")
            continue
        # ensures the feedback provided is either g, y, or w
        # the count will break the loop in case the user inputted more than 1 incorrect color
        # without the 'count' variable, the for loop would print the statement for each incorrect color the user input
        for element in feedback:
            if element not in colors:
                print('please be sure to type g, y, or w for feedback')
                count = 1
                break
        if count == 1:
            continue 

        # initialize lists that will track which letters are in which color
        greys = []
        greens = []
        yellows = []
        # add each letter to each color list
        for i in range(5):
            if feedback[i] =="w":
                greys.append(guess[i])
            elif feedback[i] == "g":
                greens.append(guess[i])
            else:
                yellows.append(guess[i])
        # if statements makes sure that the same letter is not in both (grey and green) or (grey and yellow)
        # if this was not here, it would eliminate words with more than one count of the same letter
        # the loop will restart and user will have to type in word and feedback again if this happens
        if bool(set(greys) & set(greens)) == True:
            print("Error: cannot have a letter be in green and grey at the same time.")
            print("If a letter appears more than one time- and one of those tiles is green or yellow while the other tile is grey- please enter the grey tile as yellow")
            print("For example, if 'agree' shows up as yywwg, please enter 'yywyg' into feedback")
            print("Please try again")
            continue
        if bool(set(greys) & set(yellows)) == True:
            print("Error: cannot have a letter be in yellow and grey at the same time.")
            print("Please try again")
            continue
        # when the program has made it this far, everything about the users input is good, and the while true loop breaks
        break

    # if all tiles are green, the game is over and the loop breaks
    if feedback == "ggggg":
        print("nice! you won the big game and you only had to use this stupid program to help")
        print("maybe try expaning your vocab a little more, idiot")
        break

    # cannot make changes to a list as you iterate over it, so make current words list into a tuple
    # bc of for loop, this updates to the current possible list of words each iteration (words are removed from word list below)
    word_tuple = tuple(words)

    # iterate over each word (and each letter) in the current word list
    for word in word_tuple:
        for i in range(5):
            # remove word from list if g letter not in word
            if feedback[i] == "g" and guess[i] != word[i]:
                words.remove(word)
                break
            # remove word from list if w letter is in word
            elif feedback[i] == "w" and guess[i] in word:
                words.remove(word)
                break
            # remove word from list if y letter not in word
            elif feedback[i] == "y" and guess[i] not in word:
                words.remove(word)
                break
            # remove word from list if letter is in word but not correct place (letter is yellow, but the current word in word list
            # IS that letter (letter would be green if correct))
            elif feedback[i] == "y" and guess[i] == word[i]:
                words.remove(word)
                break
    if len(words) == 0:
        print("i think you messed something up, there are no possible words left")
        print("it definitely wasn't my fault im perfect")
        print("but you can try again")
        break
    # Print possible remaining words, counter makes sure to print only 8 words/line
    print("possible remaining words:")
    counter = 0
    for word in words:
        print(word, end = ", ")
        counter += 1
        if counter == 8:
            print("")
            counter = 0
    print("")
