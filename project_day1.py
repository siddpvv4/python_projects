# number guessing game
import random as r

c=0
z= r.randint(1,100)
while True:
    try:
        i= int(input("enter guess"))
    except:
        print("please enter valid input")
        continue
    c+=1
    if z<i:
        print("TOO HIGH :<")
        if (abs(i-z)<=10):
            print("Very close 🔥")
        else:
            print("cold❄️")
        
    elif z>i:
        print("TOO LOW :<")
        if (abs(i-z)<=10):
            print("Very close 🔥")
        else:
            print("cold❄️")
        
    else :
        
        print(f"correct guess :> in {c} attempts")
        break
