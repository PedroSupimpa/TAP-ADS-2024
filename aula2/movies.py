
#creating a class with constructor
class Movies:
    def __init__(self,name,year,budget):
        self.name = name
        self.year = year
        self.budget = budget
        self.like = 0

#creating a method
    def addLike(self):
        self.like = self.like+1


class Show:
    def __init__(self,name,year,season):
        self.name = name
        self.year = year
        self.season = season
        self.like = 0
    
    def addLike(self):
        self.like=self.like+1


movie1 = Movies(name="Tarzan", year="2000", budget=2_000_000)
show1 = Show(name="Lost", year="2005",season="8")
print("Movie Name:",movie1.name)
print("Movie year:",movie1.year)
print("Movie budget:",movie1.budget)

show1.addLike()
print(f"The show choosed is {show1.name}, with {show1.season} seasons and was lauched on {show1.year}!")
print(f"The show has {show1.like} like(s)!")

movie1.addLike()
movie1.addLike()
movie1.addLike()
print(movie1.like)

