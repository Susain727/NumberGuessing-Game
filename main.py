import random

print("Hi welcome to the number guessing game. \nyou have 7 chances to guess the number. BEST OF LUCK")

low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

print(f"you have 7 chances to guess the number between {low} and {high}")


num = random.randint(low, high)
# total allowed chance(ch)
ch = 7 

# Guess counter
gc = 0

while gc<ch:
    gc +=1
    guess = int(input("Guess a number: "))

    if guess == num:
        print(f"hooray, the number is {num}. you guessed in {gc} attempt")
        break
    elif gc>=ch and guess !=num:
        print(f"opps, the number is {num}. Better Luck Next Time")
        
    elif guess > num:
        print("Try a lower number")

    elif guess < num:
        print ("try a higher number")
    