from datetime import date

class Goose:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date
        self.swimming = True


    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

nikita_goosechev = Goose("Nikita Goosechev", "Canada Goose", "evening", "genoa salami")

print(nikita_goosechev.feed())
print(nikita_goosechev)
