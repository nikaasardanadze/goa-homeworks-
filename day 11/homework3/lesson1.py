registered_password = 123
authorized = False

passcode = int(input("please enter your passcode"))



if passcode == registered_password:
    print("passcode is true congrats!")
authorized = True
while passcode != registered_password:
    print("try again passcode is false")

if passcode == registered_password:
    print("passcode is true congrats!")
    authorized = True