from games import NumberGuessing
from games import Handkerchief

import urwid
from games import Game


games = [cls() for cls in Game.__subclasses__()]
#
# for i in range(len(games)):
#     print("{} - {}".format(i, games[i].get_name()))

#number_guessimg = NumberGuessing()
#number_guessimg.play()

#handkerchief = Handkerchief()
#handkerchief.play()





choices = []

for game in games:
    choices.append(game.get_name())

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))


def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Games', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()