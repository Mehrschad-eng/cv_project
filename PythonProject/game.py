while True:
    import random
    import time
    List = ["computer", "programmier", "person", "username", "laptap"]
    d = random.choice(List)
    start = time.time()
    ch = input(f" {d} you have 5 seconds")
    if time.time() - start < 5:
        if ch == d:
            print("you win")
        else:
            print("you wrote wrong")
    else:
        print("your time is over")
    print(List)
    print("the number of letters in a word =", len(d))
    a = input("enter a letter")
    if a == d:
        print("congratulations, you have entered the next stage")
        x = 0
        while True:
            try:
                a = random.randint(1, 6)
                y = int(input("1 to roll an ace"))
                if y == 1:
                    if a == 6:
                        print("score")
                        print(a)
                    else:
                        x += 1
                        print(a)
                else:
                    break
            except ValueError:
                print("do not enter str")
            finally:
                print("done")
        print(x)