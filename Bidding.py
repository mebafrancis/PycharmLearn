
dictionarybidders = {}
bidexists= "yes"
while bidexists=="yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid value: "))
    dictionarybidders[name] = bid
    bidexists = input("Do you want to add another bidder? (yes/no): ")
    if bidexists.lower()!="yes":
        break
    else:
        print("\n"*20)

highest_bidder = max(dictionarybidders, key=dictionarybidders.get)
print("The highest bidder is", highest_bidder, "with a bid of", dictionarybidders[highest_bidder])

