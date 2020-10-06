correct = "guitar"
user = ""
a = 0
d = 3
c = 3
out_of_guesses = False

while user != correct and not(out_of_guesses):
    if a < c:
        user = input ("Enter your guess: ")
        a = a + 1
    else:
        out_of_guesses = True
if user == correct:    
    print("You Win")
else:
    print("you lose")
