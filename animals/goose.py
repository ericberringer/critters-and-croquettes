from datetime import date

class Goose:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date
        self.swimming = True

nikita_goosechev = Goose("Nikita Goosechev", "Canada Goose", "evening")

print(f'{nikita_goosechev.name} the {nikita_goosechev.species} is available to pet during the {nikita_goosechev.shift} shift.')