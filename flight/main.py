from utilities import getNumber
from flight import Flight
import constants

def readFlights(): #read flights from reservations.txt
    flightArray = []

    f = open("reservations.txt", "r")
    numFlights = int(f.readline()) #get number of flights

    for i in range(numFlights): #add flight to flight array iterate to number of flights
        flightArray.append(Flight())
        flightArray[i].readFlight(f)
    f.close()
    return flightArray, numFlights

def writeFlights(flightArray, numFlights):
    f = open("reservations2.txt", "w")
    f.write(str(numFlights) + "\n")

    for i in range(numFlights):
        flightArray[i].writeFlight(f)
    f.close()

def printFlights(flightArray, numFlights): #print flightNum, origin, destination
    print("Flight#".ljust(10), "Origin".ljust(20), "Destination".ljust(20))
    for i in range(numFlights):
        print(str(flightArray[i].flightNum).ljust(10), flightArray[i].origin.ljust(20),\
        flightArray[i].destination.ljust(20))
    print()

def addPassenger(flightArray, numFlights): #get flight number and add passenger
    printFlights(flightArray, numFlights)
    valid = False #flag to check if input flight num is valid
    i = 0
    while True:
        print("Flight number (0 = exit): ", end="")
        fltNum = getNumber()
        for i in range(numFlights): #check all flights
            if fltNum == flightArray[i].flightNum: #flight found, add passenger
                valid = True
                flightArray[i].addPassenger()
                break
        # print(i)
        if fltNum > 0 and i == numFlights - 1: #check if flight num is available
            print("We do not have flight number ", fltNum)
            print("Please try again.\n")

        # print(valid)
        if fltNum == constants.EXIT or valid == True: #exit or found flight num
            print("Returning to menu.\n")
            break

def removePassenger(flightArray, numFlights):
    printFlights(flightArray, numFlights)
    valid = False #flag to check if input flight num is valid
    i = 0
    while True:
        print("Flight number (0 = exit): ", end="")
        fltNum = getNumber()
        for i in range(numFlights): #check all flights
            if fltNum == flightArray[i].flightNum: #flight found, add passenger
                valid = True
                flightArray[i].removePassenger()
                break
        # print(i)
        if fltNum > 0 and i == numFlights - 1: #check if flight num is available
            print("We do not have flight number ", fltNum)
            print("Please try again.\n")

        # print(valid)
        if fltNum == constants.EXIT or valid == True: #exit or found flight num
            print("Returning to menu.\n")
            break

def menu(flightArray, numFlights): #initial menu
    choice = 1
    while(choice != constants.EXIT):
        print("Flight Reservation Menu\n0. Exit\n1. Add Passenger\n2. Remove Passenger\n")
        print("Please enter your choice: ", end="")
        choice = getNumber()

        if choice == constants.EXIT: #exit
            print("Goodbye.")
            return 0
        elif choice == constants.ADDPASSENGER: #add passenger
            addPassenger(flightArray, numFlights)
        elif choice == constants.REMOVEPASSENGER:
            removePassenger(flightArray, numFlights)
        else:
            print(choice, "is not an available choice.\nPlease try again\n")


def main():
    flightArray, numFlights = readFlights()
    while(menu(flightArray, numFlights) != constants.EXIT):
        pass
    writeFlights(flightArray, numFlights)


if __name__ == "__main__":
  main()
