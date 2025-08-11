print("Welcome to the rollercoaster")
height=int(input("whats your height?"))
age=int(input("whats your age?"))
bill=0;
if height>=120:
    print("you are in for a ride")
    if age<10:
        print("ticket price 10 $")
        bill=10
    elif age<=18:
        print("ticket price 15$")
        bill=15
    else:
        bill=20
        print("ticket price 20$")

    want_pic=input("Do u need the pic taken?")
    if want_pic == "y":
        bill+= 3
    print(f"Your final bill amount is{bill}")
else:
    print("Not Today")