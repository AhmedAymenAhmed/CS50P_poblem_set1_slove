#first we ask the user to input his file's name
ext=input("Enter file's name \n ").lower()
#check the extintion
if ".jpg" in ext :
    print("Image file")
elif ".jpeg" in ext:
    print("Image file")
elif ".gif" in ext:
    print("Image file")
elif ".png" in ext:
    print("Image file")
elif ".pdf" in ext:
    print("Application file")
elif ".txt" in ext :
    print("Text file")
elif "zip" in ext:
    print("Application file")
else :
    print("I don't know :( )")