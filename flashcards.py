print("Greetings")

# flashcards.py
import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    
    #initialize total as the lenghth of the cards array
    total = len(data["cards"])
    # initialize score as 0
    score=0

    for i in data["cards"]:
        guess=input(i["q"] + " > ")

        if guess == i ["a"]:
            # increment score up one
            score += 1
            # interpolate score anf total into the response
            print(f"Correct! Current score: {score}/{total}")
        else:
            print("Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")
           
