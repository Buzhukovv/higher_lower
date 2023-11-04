from art import logo, vs
from data import data
import random
import os

def clear_console():
    os.system('clear')
def text_editor(val):
    txt = str(f"{val['name']}, a {val['description']}, from {val['country']}.")
    return txt
def compare(a, b, choice):
    if a < b:
        return choice == 'b'
    else:
        return choice == 'a'
def give_random_number():
    val = random.choice(data)
    return val
def game():
    playing = True

    a = give_random_number()
    b = give_random_number()

    score = 0
    while playing:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        a_text = text_editor(a)

        a = b
        while a == b:
            b = give_random_number()
        b_text = text_editor(b)

        print(f"Compare A: {a_text}")
        print(vs)
        print(f"Against B: {b_text}")

        foll_number_a = a['follower_count']
        foll_number_b = b['follower_count']


       # print(a['follower_count'], b['follower_count'])


        more_foll = input("Who has more followers? Type 'A' or 'B':").lower()
        maxim = compare(foll_number_a, foll_number_b, more_foll)

        if maxim == False:
            clear_console()
            print(f"Sorry, that's wrong. Final score: {score}")
            playing = False

        else:
            score += 1
            clear_console()

game()