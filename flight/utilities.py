import constants

def getNumber():

    valid = False
    while(not valid):
        str = input()

        if str.isdigit():
            valid = True
            return int(str)
        else:
            print("Your number is invalid.\nPlease try again\n")
            return constants.ERROR
