import random

class Student:
    print("Hi")
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I'll sleep!")
        self.gladness += 3

    def to_chill(self):
        print("Time to rest")
        self.gladness += 5
        self.progress -= 0.1

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life."
        print(f"{day:=^50}")
        choose = random.randint(1,3)
        if choose == 1:
            self.to_study()
        elif choose == 2:
            self.to_sleep()
        elif choose == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student("Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)