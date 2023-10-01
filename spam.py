import pyautogui
from time import sleep

n = input("How many message do you want to send?\n")
msg = input("What is your message?\n")

n = int(n)

print("Please select the message fild and wait...")

sleep(10)

print("The program is starting!")

while True:      
    pyautogui.typewrite(msg) 
    sleep(.250)                        
    pyautogui.typewrite("\n")                                    

    n = n - 1        

    print("{} messages left.".format(n))

    if n == 0:
        break


print("All the messages was sent!")       
