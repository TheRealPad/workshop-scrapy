def exercice01(min, max):
    for i in range(min + 1, max + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 5 == 0:
            print("Five")
        elif i % 3 == 0:
            print("Three")
        else:
            print(i)

if __name__ == "__main__":
    exercice01(0, 100)