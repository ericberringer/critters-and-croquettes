from datetime import date

class Llama:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date
        self.walking = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}."

como_se_llama = Llama("Como Se Llama", "domestic llama", "afternoon", "eggs benny")

print(como_se_llama.feed())
print(como_se_llama)
