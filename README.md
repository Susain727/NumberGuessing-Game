# NumberGuessing-Game
Welcome to a fun beginner project designed just for those starting their journey with Python! In this project, we’ll create a simple number guessing game that invites you to discover a randomly chosen number within a range you set.
<br>
To kick things off, you’ll get to pick a range by entering a lower and an upper bound (for example, from A to B). Once you've set your range, our game will randomly select an integer from that interval. Your challenge? To guess the secret number using as few attempts as possible! After each guess, you’ll receive helpful feedback so you can adjust your next guess based on whether you were too high or too low. (Have fun and good luck!).
<br>
# Example: Guessing a number in a range from 1 to 100
<p>Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 50 → Too high<br>
Guess 2: 25 → Too low<br>
Guess 3: 37 → Too low<br>
Guess 4: 43 → Too high<br>
Guess 5: 40 → Too low<br>
Guess 6: 41 → Too low<br>
Guess 7: 42 → Correct!<br>

Total Guesses: 7
</p>

# Algorithm
<pre>
Accept lower and upper bounds from the user.<br>
Generate a random number in the selected range.<br>
Calculate the maximum allowed guesses using the binary search formula.<br>
Run a loop to take user guesses:<br>
    If the guess is too high, print: "Try Again! You guessed too high."<br>
    If the guess is too low, print: "Try Again! You guessed too small."<br>
    If the guess is correct, print: "Congratulations!" and exit the loop.<br>
    If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"
</pre>