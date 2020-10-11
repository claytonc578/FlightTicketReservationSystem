import re

from person import Person
from utilities import getNumber
import constants

class Plane:
    def __init__ (self):
        self.rows = 0
        self.width = 0
        self.reserved = 0
        self.passengers = {}
        self.isOccupied = [[False] * 1] * 1

    def readPlane(self, f):
        planeinfo = f.readline() #get plane info: rows, width, and number of reserved seats
        intstr = re.findall(r'\d+', planeinfo)
        self.rows = int(intstr[0])
        self.width = int(intstr[1])
        self.reserved = int(intstr[2])
        # print(self.rows, self.width, self.reserved)
        self.isOccupied = [[False for i in range(self.width)] for j in range(self.rows)]

        for i in range(self.reserved): #get each Passenger seat number and name
            passengerinfo = f.readline()
            infolist = re.sub("[^\w]", " ",  passengerinfo).split()
            # print(infolist[0], infolist[1], infolist[2])
            seat = infolist[0]
            self.passengers[seat] = Person(infolist[0], infolist[1], infolist[2]) #insert person into dictionary: key = seatnum, value = person

            seat = list(seat) #modify if 2D array of boolean isOccupied
            row = ord(seat[0]) - ord('0') - 1
            col = ord(seat[1]) - ord('A')
            # print("adding Person", row, col)
            self.isOccupied[row][col] = True
        # print(self.isOccupied)
        # for x, y in self.passengers.items():
        #     print(x, y.firstname)

    def printOccupied(self):
        #print occupied and available seats
        print("Row#".ljust(5), end="")
        for r in range(self.width): #print row
            print(chr(r + ord('A')), end="")
        print()
        for r in range(self.rows): #print isOccupied
            print(str(r+1).ljust(5), end="")
            for c in range(self.width):
                if self.isOccupied[r][c] == True:
                    print("X", end="")
                else:
                    print("-", end="")
            print("")
        print("\nX = reserved\n")

    def addPassenger(self):
        #get first and last name of passenger to be added
        fname = input("Please enter first name of passenger: ")
        lname = input("Please enter last name of passenger: ")

        #print occupied and available seats
        self.printOccupied()

        #get user input for row
        inputrow = 0
        inputseat = '0'
        validseat = False

        while (inputrow <= 0 or inputrow > self.rows) or (validseat == False):
            print("Please enter the row of the seat you wish to reserve: ", end="")
            inputrow = getNumber()
            if inputrow == constants.ERROR: #check if valid number
                continue
            if inputrow <= 0 or inputrow > self.rows: #check if valid row#
                print("There is no row #{}".format(inputrow), "on this flight.\nPlease try again.\n")
                continue

            #get user input for seat letter
            while (ord(inputseat) < ord('A') or ord(inputseat) >= ord('A') + self.width) or (validseat == False):
                print("Please enter seat letter you wish to reserve on row #{}: ".format(inputrow), end="")
                inputseat = input()

                if ord(inputseat) < ord('A') or ord(inputseat) >= ord('A') + self.width: #check if valid seat letter
                    print("Seat letter invalid.\nPlease try again.\n")
                elif self.isOccupied[inputrow-1][ord(inputseat) - ord('A')] == True: #check if occupied
                    print("That seat is already occupied\nPlease try again.\n")
                    break
                else:
                    validseat = True
                    self.isOccupied[inputrow-1][ord(inputseat) - ord('A')] = True #mark seat as occupied
                    key = str(inputrow) + inputseat
                    self.passengers[key] = Person(key, fname, lname) #add Person to hashmap
                    print("{} {} has been added to {}".format(fname, lname, key))

    def removePassenger(self):
        #print occupied and available seats
        self.printOccupied()
        
        #get user input for row
        inputrow = 0
        inputseat = '0'
        validseat = False

        while (inputrow <= 0 or inputrow > self.rows) or (validseat == False):
            print("Please enter the row of the seat you wish to remove: ", end="")
            inputrow = getNumber()
            if inputrow == constants.ERROR: #check if valid number
                continue
            if inputrow <= 0 or inputrow > self.rows: #check if valid row#
                print("There is no row #{}".format(inputrow), "on this flight.\nPlease try again.\n")
                continue

            #get user input for seat letter
            while (ord(inputseat) < ord('A') or ord(inputseat) >= ord('A') + self.width) or (validseat == False):
                print("Please enter seat letter you wish to remove on row #{}: ".format(inputrow), end="")
                inputseat = input()

                if ord(inputseat) < ord('A') or ord(inputseat) >= ord('A') + self.width: #check if valid seat letter
                    print("Seat letter invalid.\nPlease try again.\n")
                elif self.isOccupied[inputrow-1][ord(inputseat) - ord('A')] == False: #check if occupied
                    print("That seat is already unoccupied\nPlease try again.\n")
                    break
                else:
                    validseat = True
                    self.isOccupied[inputrow-1][ord(inputseat) - ord('A')] = False #mark seat as open
                    key = str(inputrow) + inputseat
                    print("{} {} has been removed to {}".format(self.passengers[key].firstname, self.passengers[key].lastname, key))
                    del self.passengers[key] #remove Person from dictionary





#end file
