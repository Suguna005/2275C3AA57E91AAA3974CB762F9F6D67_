"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtlelayer:

  def play(self):
    print("The player is playing cricket.")


class Batsman(player):

  def play(self):
    print("The batsman is batting.")


class Bowler(player):

  def play(self):
    print("The bowler is bowling.")


batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()


# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
  t.color(c)
  t.forward(75)
  t.left(90)