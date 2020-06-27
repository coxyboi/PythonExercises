def main():

    initial = eval(input("What was the initial deposit, faggot? "))
    apr = 0.03
    total = initial
    years = 0

    while total < initial * 2:
        total *= 1 + apr
        years += 1
        print(total)

    print("It takes", years, "years to double ")
    print("your investment at an interest rate of " + str(apr*100) + "%")


main()