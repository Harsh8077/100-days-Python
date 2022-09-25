#-----------------------------Bidding Game------------------------------------
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("-------------------------Bidding Game-------------------------")

def winner(c1, c2, p1, p2):
    if c1 > c2:
        print(f"{p1} has Won the Bidding Game!!")
    else:
        print(f"{p2} has won the Bidding Game!!")


def item3(p1, a1, p2, a2, c1, c2):
    print("Bidding for Invisible Power is Starting")
    bid = "yes"
    while bid == "yes":
        print(f"Its {p1} chance you have {a1} amount")
        bidAmount1 = int(input("Enter your bid amount $"))
        print(f"Its {p2} chance you have {a2} amount")
        bidAmount2 = int(input("Enter you bid amount $"))
        if bidAmount1 >= bidAmount2:
            print(f"Highest bidder is {p1} with the bid of {bidAmount1}")
            buyyer = p1
            spend = bidAmount1

        else:
            print(f"Highest bidder is {p2} with the the bid of {bidAmount2}")
            buyyer = p2
            spend = bidAmount2

        bid = input("Do you still want to bid?yes/no ")
    print(f"Congratulation!! {buyyer} you bought the Invisible Power at {spend}$ ")
    if buyyer == p1:
        a1 = a1 - spend
        c1+=1
    else:
        a2 = a2 - spend
        c2+=1
    print(f"{p1} have {a1}$ in his account and {p2} has {a2}$ in his account")
    winner(c1, c2, p1, p2)


def item2(p1, a1, p2, a2, c1, c2):
    print("Bidding for Mystery Spell is Starting")
    bid = "yes"
    while bid == "yes":
        print(f"Its {p1} chance you have {a1} amount")
        bidAmount1 = int(input("Enter your bid amount $"))
        print(f"Its {p2} chance you have {a2} amount")
        bidAmount2 = int(input("Enter you bid amount $"))
        if bidAmount1 >= bidAmount2:
            print(f"Highest bidder is {p1} with the bid of {bidAmount1}")
            buyyer = p1
            spend = bidAmount1

        else:
            print(f"Highest bidder is {p2} with the the bid of {bidAmount2}")
            buyyer = p2
            spend = bidAmount2

        bid = input("Do you still want to bid?yes/no ")
    print(f"Congratulation!! {buyyer} you bought the Mystery Sword at {spend}$ ")
    if buyyer == p1:
        a1 = a1 - spend
        c1+=1
    else:
        a2 = a2 - spend
        c2+=1
    print(f"{p1} have {a1}$ in his account and {p2} has {a2}$ in his account")
    item3(p1, a1, p2, a2, c1, c2)


def item1(p1, a1, p2, a2, c1, c2):
    print("Bidding for Golden Sword is Starting")

    bid = "yes"
    while bid == "yes":
        print(f"Its {p1} chance you have {a1} amount")
        bidAmount1 = int(input("Enter your bid amount $"))
        print(f"Its {p2} chance you have {a2} amount")
        bidAmount2 = int(input("Enter you bid amount $"))
        if bidAmount1 >= bidAmount2:
            print(f"Highest bidder is {p1} with the bid of {bidAmount1}")
            buyyer = p1
            spend = bidAmount1

        else:
            print(f"Highest bidder is {p2} with the the bid of {bidAmount2}")
            buyyer = p2
            spend = bidAmount2

        bid = input("Do you still want to bid?yes/no ")
    print(f"Congratulation!! {buyyer} you bought the Golden Sword at {spend}$ ")
    if buyyer == p1:
        a1 = a1 - spend
        c1+=1
    else:
        a2 = a2 - spend
        c2+=1
    print(f"{p1} have {a1}$ in his account and {p2} has {a2}$ in his account")
    item2(p1, a1, p2, a2, c1, c2)


p1 = input("Enter the name of player 1")
p2 = input("Enter the name of player 2")
print("You both have 1000$ as total bid amount each, you have to buy 3 items")
a1 = 1000
a2 = 1000
c1 = 0
c2 = 0
item1(p1, a1, p2, a2, c1, c2)
