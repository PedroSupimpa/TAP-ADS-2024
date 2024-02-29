
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
        self.__name = name
        self.year = year
        self.season = season
        self.starsCount = 0

    
    def addStars(self):
        self.starsCount = self.starsCount+1

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name


movie1 = Movies(name="Tarzan", year="2000", budget=2_000_000)
show1 = Show(name="Lost", year="2005",season="8")
print("Movie Name:",movie1.name)
print("Movie year:",movie1.year)
print("Movie budget:",movie1.budget)

show1.addStars()
show1.addStars()
print(f"The show choosed is {show1.name}, with {show1.season} seasons and was lauched on {show1.year}!")
print(f"The show has {show1.starsCount} stars!")

show1.name = "Losted"
print(show1.name)

movie1.addLike()
movie1.addLike()
movie1.addLike()
print(movie1.like)

#using class super
class specialMovies(Movies):
    def __init__(self, name, year, budget):
        super().__init__(name, year, budget)



special = specialMovies(name="Transformers", year="2011", budget=100_000_000)
print(special.name)
