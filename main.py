from games import NumberGuessing
from games import Handkerchief

from games import Game


games = [cls() for cls in Game.__subclasses__()]

for i in range(len(games)):
    print("{} - {}".format(i, games[i].get_name()))

#number_guessimg = NumberGuessing()
#number_guessimg.play()

#handkerchief = Handkerchief()
#handkerchief.play()