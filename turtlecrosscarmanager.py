import random
from turtlecrosscarmodel import Car


LANES = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]
DIFFICULTY_NORMAL = 40


class CarManager:


    def __init__(self):
        self.cars = []
        self.carsallowedperlane = 0
        self.difficulty = DIFFICULTY_NORMAL
        self.nextlevel()


    def islanefull(self, lane):
        carsinlane = 0
        for car in self.cars:
            if car.lane == lane:
                carsinlane += 1
        if carsinlane >= self.carsallowedperlane:
            return True
        else:
            return False
    

    def islanesfull(self):
        fulllanes = 0
        for lane in LANES:
            if self.islanefull(lane):
                fulllanes += 1
        if fulllanes >= len(LANES):
            return True
        else:
            return False


    def addcar(self):
        lane = random.choice(LANES)
        if self.islanefull(lane) == False:
            newcar = Car(lane)
            newcar.difficulty = self.difficulty
            self.cars.append(newcar)


    def movecars(self):
        for car in self.cars:
            car.move()
            if car.x < -500:
                car.reset()
                

    def nextlevel(self):
        self.carsallowedperlane += 1
        while self.islanesfull() == False:
            self.addcar()
