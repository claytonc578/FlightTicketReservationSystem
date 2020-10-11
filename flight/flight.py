from plane import Plane

class Flight:
    def __init__(self):
        self.flightNum = 0
        self.origin = ""
        self.destination = ""
        self.plane = Plane()

    def readFlight(self, f): #read flight info: flightNum, origin, destination, Plane
        self.flightNum = int(f.readline())
        origin = f.readline()
        origin = origin.strip()
        self.origin = origin
        destination = f.readline()
        destination = destination.strip()
        self.destination = destination
        # print(self.flightNum, self.origin, self.destination)
        self.plane.readPlane(f)

    def writeFlight(self, f):
        f.write(str(self.flightNum) + "\n")
        f.write(self.origin + "\n")
        f.write(self.destination + "\n")

    def getFlightNumber(self): #return flightNum
        return self.flightNum

    def addPassenger(self): #add passenger to flight.plane
        self.plane.addPassenger()

    def removePassenger(self):
        self.plane.removePassenger()
