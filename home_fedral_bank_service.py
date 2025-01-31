#we want to ask the user to greet
greet=input("hello \n").lower()
#if the user said something starts with h but not hellp he will pay 20$ if he said hello he won't pay any thing else he will pay 100$
if "hello" in greet:
    print("0$")
elif "h" in greet[0] :
    print("20$")
else :
    print("100$")