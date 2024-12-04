# Syntax


# if condition:
#     stmt1

# elif condition2:
#      stmt2

# elif condition3:
#     stmt3

# else:
#     default stmt  



signal=input("Enter the Signal:").lower()

if signal=="red": #RED ==red

    print("STOP")

elif signal=="green":

    print("Go...")

elif signal=="orange":

    print("Wait..!")    

else:
    print("Invalid signal")        