# NumberGuessing-Game
Welcome to a fun beginner project designed just for those starting their journey with Python! In this project, we’ll create a simple number guessing game that invites you to discover a randomly chosen number within a range you set.
<br>
To kick things off, you’ll get to pick a range by entering a lower and an upper bound (for example, from A to B). Once you've set your range, our game will randomly select an integer from that interval. Your challenge? To guess the secret number using as few attempts as possible! After each guess, you’ll receive helpful feedback so you can adjust your next guess based on whether you were too high or too low. (Have fun and good luck!).
<br>
# Example 1: Guessing in a range from 1 to 100
<pre>
Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 50 → Too high
Guess 2: 25 → Too low
Guess 3: 37 → Too low
Guess 4: 43 → Too high
Guess 5: 40 → Too low
Guess 6: 41 → Too low
Guess 7: 42 → Correct!

Total Guesses: 7
</pre>

# Example 2: Guessing in a range from 1 to 50
<pre>
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 25 → Too low
Guess 2: 37 → Too low
Guess 3: 43 → Too high
Guess 4: 40 → Too low
Guess 5: 41 → Too low
Guess 6: 42 → Correct!

Total Guesses: 6
</pre>
# Algorithm
<pre>
Accept lower and upper bounds from the user.
Generate a random number in the selected range.
Calculate the maximum allowed guesses using the binary search formula.
Run a loop to take user guesses:
    If the guess is too high, print: "Try Again! You guessed too high.
    If the guess is too low, print: "Try Again! You guessed too small.
    If the guess is correct, print: "Congratulations!" and exit the loop.
    If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"
</pre>