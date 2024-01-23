class Person:
    def __init__(self, initialAge: int):
        # Constructor method to initialize the Person object with an age
        if initialAge < 0:
            # Check if the initial age is negative
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            # Set the age to the provided initialAge if it's non-negative
            self.age = initialAge

    def amIOld(self) -> None:
        # Method to determine and print the age category of the person
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self) -> None:
        # Method to simulate the passage of one year, incrementing the age
        self.age += 1


# The rest of the code remains unchanged.


# HackerRank test
# t = int(input())
# for i in range(0, t):
#     age = int(input())         
#     p = Person(age)  
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")