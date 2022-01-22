from game.card import Card

"""
Game Order:
    1. Displays first card
    2. Is next card going to be higher or lower?
    3. Displays the next card
    4. Displays updated Score
    5. Play again?
"""

class Director:
    # set card to string
    # set playing to True
    # start with 300 points
    def __init__(self):
        self.card = ""
        self.is_playing = True
        self.score = 300
        
    # start game play
    def start_game(self):
        
        # while loop for steps in game 
        while self.is_playing:
            print("")
            self.get_card1()
            self.get_hilo()
            self.get_card2()
            self.display_score()
            self.play_again() 
            
    # Step one: Get first card -- Call from card.py for draw card action. 
    def get_card1(self):
        self.card1 = Card.draw(self)
        print(f"The card is: {self.card1}")

    # Step two: Player choose High or Low.
    def get_hilo(self):
        self.choice = ""
        while not (self.choice.lower() == "l" or self.choice.lower() == "h"):
            self.choice = input("Higher or lower? [h/l] ")
            
    # Step three: Get the next card -- Call from card.py for draw card action.
    def get_card2(self):
        self.card2 = Card.draw(self)
        while self.card2 == self.card1:
            self.card2 = Card.draw(self)
        print(f"Next card was: {self.card2}")
        
    # Step four: Determine score by testing card1 vs. card2 and hilo input.
    def display_score(self):
        if self.card1 > self.card2 and self.choice.lower() == "l":
            self.score += 100
            print(f"Correct! Your new score is: {self.score}")
        elif self.card1 < self.card2 and self.choice.lower() == "h":
            self.score += 100
            print(f"Correct! Your new score is: {self.score}")
        elif self.card1 > self.card2 and self.choice.lower() == "h":
            self.score -= 75
            print(f"Incorrect: Your new score is: {self.score}")
        elif self.card1 < self.card2 and self.choice.lower() == "l":
            self.score -= 75
            print(f"Incorrect: Your new score is: {self.score}")
        else:
            self.score = self.score  
            print("Something Goofed here...") 
            
    # Step five: Check if user has less than 0 points and end game or Ask user if they want to play again.
    def play_again(self):
        if self.score <= 0:
            print("\nGAME OVER: Your ran out of points")
            self.is_playing = False
        else:
            again = input(f"Play Again? [y/n] ")
            if again.lower() == "n":
                self.is_playing = False
                print("\nThank you for playing!")
        
