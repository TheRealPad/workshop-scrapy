def calculate(calcul):
    total = 0
    if type(calcul) == list:
        for row in calcul:
            if type(row) == str:
                if row.lstrip("-").isdigit():
                    total = total + int(row)
        return total
    else:
        return False

if __name__ == "__main__":
    print(calculate(['4', '3', '-2']))
    print(calculate(453))
    print(calculate(['nothing', 3, '8', 2, '1']))
    print(calculate('54'))