while True:
    try:
        x = int(input("enter a number:"))
        y = int(input("enter another number:"))
        z = x / y
        print("the answer is divided : ", z)
    except ZeroDivisionError:
        print("the number 0 is not divisible.enter another number")
    except ValueError:
        print("str is not a divisible.enter a number")
    else:
        print("run without error")
    finally:
        print("done")