#!/usr/bin/env python

import random

def main():
 """Start a song guessing game."""
 print("Guess the Song! no need to put caps lock")

 x = ("golden hour")
 guess = None

 while x != guess:

    guess = str(input("Pick a song: "))

    if x == guess:
       print("You're Correct SLAY!")
    else:
       print("It was viral last year.The singer is a male.2 words.The first word is in the periodic table.")
main()