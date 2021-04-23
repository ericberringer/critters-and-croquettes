from datetime import date

class Snake:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

chris_nake = Snake("Chris Nake", "king snake", "morning", "one glazed donut")

print(chris_nake.feed())
print(chris_nake)