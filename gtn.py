import random

print("*" * 20, "GUESS THE NUMBER", "*" * 20)

levels = 9
print("1 - EASY\t2 - NORMAL\t3 - HARD")

opt1 = int(input("PLEASE ENTER THE NUMBER OF YOUR PREFERRED LEVEL OF DIFFICULTY\n"))
if opt1 <= 0:
    while opt1 <= 0:
        opt1 = int(input("INAPPLICABLE. REENTER LEVEL OF DIFFICULTY\n"))


def guess_the_number(n):
    i = 3
    while i < n:
        print("OUT OF BOUNDS. REENTER OF DIFFICULTY LEVEL\t")
        n = int(input())

    a = 1
    b = 0
    if n == 1:
        b = b + 10
        print("\nGUESS FROM NUMBERS 1-10")
    elif n == 2:
        b = b + 50
        print("\nGUESS FROM NUMBERS 1-50")
    elif n == 3:
        b = b + 100
        print("\nGUESS FROM NUMBERS 1-100")

    x = random.randint(a, b)
    j = 1
    while j <= 3:
        guess = int(input("ENTER YOUR GUESSED NUMBER: "))
        j = j + 1

        if x < guess:
            print("TOO HIGH")
        elif x > guess:
            print("TOO LOW")
        else:
            print("\nCORRECT")
            break

    if x != guess:
        print("\nGAME OVER")


guess_the_number(opt1)
