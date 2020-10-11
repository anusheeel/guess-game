import json
import requests
import random
import string

dummy = string.ascii_lowercase
correct = random.choice(dummy)
user = ""
guess_count = 0
coin_remaining = 3
guess_limit = 3
not_enough_coin = False
api_url = 'https://opentdb.com/api.php?amount=1&difficulty=easy'
print("Welcome!! This is a boring guessing game")

def questions(api_url):
    obj = ['question']
    r = requests.get(api_url)
    s = r.json(obj)
    print(s)

while user != correct and not(not_enough_coin):
    if guess_count < guess_limit and coin_remaining != guess_count:
        print( f"You have {coin_remaining} coins in hand")
        coin_remaining -= 1
        user = input ("Enter your guess: ")
        guess_count += 1
        
    else:
        print("You are Out of Coins, ")
        print("Answer the following questions to get an extra coin")
        questions(api_url)
        not_enough_coin = True
if user == correct:    
    print("Congratulations !! You Win")
else:
    print("You Lose")
