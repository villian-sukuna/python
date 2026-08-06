from abc import ABC, abstractmethod

# 1 & 2. Create Abstract Class Shape
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# 3. Child Class Rectangle
class Rectangle(Shape):

    # 4. Accept length and breadth
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Implement abstract method
    def area(self):
        return self.length * self.breadth

    # Implement abstract method
    def perimeter(self):
        return 2 * (self.length + self.breadth)


# 5. Create object and display results
length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

rect = Rectangle(length, breadth)

print("\n--- Rectangle Details ---")
print("Area =", rect.area())
print("Perimeter =", rect.perimeter())