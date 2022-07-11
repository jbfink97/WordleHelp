# WordleHelp
### Easy to use command line program to help you win wordle
***
This program prints a list of all possible remaining words in Wordle after you input your guess word and the colors of the tiles for that word.

For example, if you typed in "weary" as a guess on Wordle and it resulted in the image below:

![weary](/images/weary.PNG)

The next steps would be to type "weary" as the "guess word" in the command line.
After that, type the corresponding tile colors for "feedback" when prompted. ("g" if the tile is green, "y" if yellow, and "w" if grey/wrong).
The corresponding is how you should type in the "weary" example above into the command line.

![wearyguess](/images/wearyguess.PNG)

Since the "w", "e", "r", and "y" tiles in "weary" were greyed out, they get a "w" for their spots in the "feedback" input. The "a" in "weary" was yellow,
so its spot gets "y".

The program then prints a list of all possible remaining words to guess. Repeat this process until you win!

__An important note__: if you enter a word where a letter occurs more than one time, with one letter being grey and the other one being green or yellow,
please make sure to enter the grey'd out letter as yellow

In the example below, "adder" has one "d" with a grey tile and one "d" with a green tile.
For the "feedback" prompt, the user would need to enter the "d" with the grey tile as yellow since a letter cannot be both in the word (green tile) and missing
from the word (grey tile) at the same time.



The resulting feedback would need to be entered as: "yygww"
