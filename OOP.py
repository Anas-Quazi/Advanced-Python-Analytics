#* ------------------ F1 OOP examples (no imports) ------------------

#* basic class/object – driver
class Driver:
    series = "Formula 1"
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self._points = 0
    def introduce(self):
        print(f"Driver {self.name}, number {self.number}")

d = Driver("Lewis Hamilton", 44)
d.introduce()

#~ ------------------------------------------------------

#* encapsulation – team account
class TeamAccount:
    def __init__(self, budget=0):
        self._budget = budget
    def cost(self, amount):
        if amount < 0:
            raise ValueError("negative cost")
        self._budget -= amount
    def add_sponsor(self, amount):
        if amount < 0:
            raise ValueError("negative money")
        self._budget += amount
    def get_budget(self):
        return self._budget

acct = TeamAccount(1000000)
acct.cost(250000)
print("Budget left:", acct.get_budget())

#* “abstraction” without abc – just a base class with methods to override
class Car:
    def top_speed(self):
        raise NotImplementedError
    def accelerate(self):
        raise NotImplementedError

class Ferrari(Car):
    def __init__(self, model):
        self.model = model
    def top_speed(self): return 350
    def accelerate(self): return "vroom"

#* inheritance & polymorphism – teams
class TeamMember(Driver):
    def __init__(self, name, number, team):
        super().__init__(name, number)
        self.team = team
    def introduce(self):
        print(f"{self.name} drives for {self.team}")

class Engineer(TeamMember):
    def introduce(self):
        print(f"Engineer {self.name} at {self.team}")

people = [TeamMember("Max Verstappen", 1, "Red Bull"),
          Engineer("James Allison", 0, "Mercedes")]
for person in people:
    person.introduce()

#~ ------------------------------------------------------

#* overriding vs overloading
class RaceStats:
    def laps(self, a, b, c=None):
        if c is None:
            return a + b
        return a + b + c

rs = RaceStats()
print(rs.laps(1,2), rs.laps(1,2,3))

#* operator overloading – lap time addition
class LapTime:
    def __init__(self, seconds):
        self.seconds = seconds
    def __add__(self, other):
        return LapTime(self.seconds + other.seconds)
    def __repr__(self):
        return f"{self.seconds:.3f}s"

print(LapTime(72.345) + LapTime(73.210))

#* class & static methods – constructors
class ConstructorStandings:
    points = 0
    def __init__(self):
        ConstructorStandings.points += 1
    @classmethod
    def total(cls):
        return cls.points
    @staticmethod
    def info():
        print("Points for constructors")

print(ConstructorStandings.total())
ConstructorStandings.info()

#* property – tyre temps
class Tyre:
    def __init__(self, temp=20):
        self._temp = temp
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, t):
        if t < 0:
            raise ValueError("cold tyre")
        self._temp = t

tyre = Tyre()
tyre.temp = 85
print("Tyre temp:", tyre.temp)

#* multiple inheritance – driver who can engineer
class Strategist:
    def strategize(self): print("planning pit stops")
class Tester:
    def test(self): print("testing setup")
class MultiRole(Strategist, Tester): pass

mr = MultiRole()
mr.strategize(); mr.test()

#* class decorator – add repr
def add_repr(cls):
    def __repr__(self): return f"<{cls.__name__}>"
    cls.__repr__ = __repr__
    return cls

@add_repr
class PitCrew: pass

print(PitCrew())

#* manual “dataclass” equivalent
class Chassis:
    def __init__(self, weight, drag):
        self.weight = weight
        self.drag = drag
    def __repr__(self):
        return f"Chassis(weight={self.weight}, drag={self.drag})"

print(Chassis(750, 0.32))