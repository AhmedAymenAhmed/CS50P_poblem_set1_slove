#Ask the user about the time

flag ="yes"
while flag=="yes":
    try :
        time=input("what is the time in #:## form ?")
        time=time.replace(":",".")
        float(time)
        flag="no"
    except ValueError:
        print("Enter in #:## form please")
if "7." in  time :
    print("Break fast time")
elif time=="8.00" :
    print("Break fast time ended")
elif "12." in time:
    print("Lunch time ")
elif time =="13.00" :
    print("Lunch time ended ")
elif "18." in time:
    print("dinner time ")
elif time =="19.00" :
    print("dinner time ended ")
else :
    print("Not a meal time")
