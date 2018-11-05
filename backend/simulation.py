import csv
import time
import random



cars = []

map = []
with open("map.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        map.append(row)
# print(map)




def junctionFUNction(car):
    print("jf", car)
    isValid = False
    while isValid == False:
        newrandom = random.randint(1,4)
        if newrandom == 1:
            newLocation = map[car["ygrid"]-1][car["xgrid"]]
            if newLocation == "2":
                isValid = True
                car["direction"] = "N"

        if newrandom == 2:
            newLocation = map[car["ygrid"]+1][car["xgrid"]]
            if newLocation == "2":
                isValid = True
                car["direction"] = "S"

        if newrandom == 3:
            newLocation = map[car["ygrid"]][car["xgrid"]+1]
            if newLocation == "2":
                isValid = True
                car["direction"] = "E"


        if newrandom == 4:
            newLocation = map[car["ygrid"]][car["xgrid"]-1]
            if newLocation == "2":
                isValid = True
                car["direction"] = "W"

        print("isValid",isValid)



def writeToText(cars):
    file = open("cars.txt", "w")
    file.write(str(cars))
    file.close()


def checkIfMoves(car, carsarray):

    # print("cim", car)
    cannotMove = False;
    for i in range(0, len(carsarray)):
        if (car["direction"] == (carsarray[i-1])["direction"]) & (car["xgrid"] == (carsarray[i-1])["xgrid"]) & ((carsarray[i])["ygrid"] == car["ygrid"]):
            cannotMove = True
        if cannotMove == False:
            print("cim true", car)
            return True;
        else:
            print("cim false", car)
            return False;




def moveCar(car):
    if car["direction"] =="N":
        car["ygrid"] = car["ygrid"]-1
    if car["direction"] == "S":
        car["ygrid"] = car["ygrid"]+1
    if car["direction"] == "E":
        car["xgrid"] = car["xgrid"]+1
    if car["direction"] == "W":
        car["xgrid"] = car["xgrid"]-1


def getTile(car):
    # print("car", car)
    # print(str(car))
    y = int(car["ygrid"])
    x = int(car["xgrid"])
    tile = str(map[y][x])
    return tile


def carMoveTurn(cararray):
    print("cmt",cararray)
    for i in range(0, len(cararray)):
        mycar = cararray[i]
        print(mycar)
        tile = getTile(mycar)
        print("tile", tile)
        if tile == "4":
            junctionFUNction(mycar)
            if checkIfMoves(mycar, cararray):
                moveCar(mycar)
        # elif (tile == "5") & (mycar["direction"] == "N"):
        #         del cararray[i-1]
        else:
            if checkIfMoves(mycar, cararray):
                moveCar(mycar)
    writeToText(cararray)

def createCar():
    newcar = {}
    newid = len(cars)
    newrandom = random.randint(1,2)
    if newrandom == 1:
        newcar = {"id": newid, "xgrid" : 27, "ygrid" : 1, "direction": "S"}
        cars.append(newcar)
    else:
        newcar = {"id": newid, "xgrid": 33, "ygrid": 1, "direction": "S"}
        cars.append(newcar)

def runSimulation():
    carsCount = 40
    currentCars = 0
    while True:
        time.sleep(1)
        carMoveTurn(cars)
        # print("cars:", cars)
        if currentCars < carsCount:
            createCar()
            currentCars = currentCars + 1

        # print("cars:", cars)

runSimulation()

