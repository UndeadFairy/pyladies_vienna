class Cat:
    def __init__(self):         # Init function does not have to take number of lives
        self.lives_number = 9   # as parameter 'cause that number is always the same.

    def meow(self):
        print("Meow, meow, meeeoooow!")

    def alive(self):
        return self.lives_number > 0

    def lose_life(self):
        if not self.alive():
            print("You can't kill a cat that is already dead, you monster!")
        else:
            self.lives_number -= 1

    def eat(self, food):
        if not self.alive():
            print("It's pointless to give food to dead cat!")
            return
        if food == "fish" and self.lives_number < 9:
            self.lives_number += 1
            print("The cat ate a fish and gained 1 life!")
        else:
            print("The cat is eating.")
