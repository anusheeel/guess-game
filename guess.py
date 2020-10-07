correct = "guitar"
user = ""
guess_count = 0
coin_remaining = 3
guess_limit = 3
not_enough_coin = False
print("Welcome!! This is a boring guessing game")

while user != correct and not(not_enough_coin):
    
    if guess_count < guess_limit and coin_remaining != guess_count:
        print( "You have", coin_remaining , "coins in hand")
        coin_remaining -= 1
        user = input ("Enter your guess: ")
        guess_count += 1
        
    else:
        print("Out of Coins")
        not_enough_coin = True
if user == correct:    
    print("Congratulations !! You Win")
else:
    print("You Lose")
