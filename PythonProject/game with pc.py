from random import randint
print("pick a number between 0 and 100 in your mind and I II guess.")
low, high = 1, 100
while 1:
    guess = randint(low, high)
   print("computer's guess: ", guess)
    vs = input("(d) true |(k) smaller |(b) bigger")
    if vs == "d":
        print("the computer succeeded")
        break
    elif vs == "b":
        low = guess + 1
    elif vs == "k":
        high = guess - 1