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

    def __init__(self):
        self.card = ""
        self.is_playing = True
        self.score = 300

    def start_game(self):
        
        while self.is_playing:
            print("")
            self.get_card1()
            self.get_hilo()
            self.get_card2()
            self.display_score()
            self.play_again()  

    def get_card1(self):
        self.card1 = Card.draw(self)
        print(f"The card is: {self.card1}")


    def get_hilo(self):
        self.choice = ""
        while not (self.choice.lower() == "l" or self.choice.lower() == "h"):
            self.choice = input("Higher or lower? [h/l] ")

    def get_card2(self):
        self.card2 = Card.draw(self)
        while self.card2 == self.card1:
            self.card2 = Card.draw(self)
        print(f"Next card was: {self.card2}")

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

    def play_again(self):
        if self.score <= 0:
            print("\nGAME OVER: Your ran out of points")
            self.is_playing = False
        else:
            again = input(f"Play Again? [y/n] ")
            if again.lower() == "n":
                self.is_playing = False
                print("\nThank you for playing!")
        
