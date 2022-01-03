# Python Classes

## Example
A **UML Class Diagram (Unified Modeling Language)** is a graphical representation of a class. It shows the **signatures** of a class’s code.

Examine the following diagram for a `Point` class.

| Point |
| :-- |
| x: float|
|y: float|
|`slope(Point): float`|
|`distance_to(Point): float`|

And here is an implementation of this class in Python:
```py
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def slope(self, other_point):
            y_diff = (self.y - other_point.y)
            x_diff = (self.x - other_point.x)
            return y_diff / x_diff

        def distance_to(self, other_point):
            y_diff = (self.y - other_point.y)
            x_diff = (self.x - other_point.x)
            return ((y_diff**2)+(x_diff**2))**0.5

    p1 = Point(0, 0)
    p2 = Point(2, 0)
    m = p2.slope(p1) # 0.0
    d = p1.distance_to(p2) # 2.0


```
1. What is the syntax for defining a class in Python?
2. What is stored in the variable `p1`?
3. What does the `slope()` function do, and how is it used?


## Theory
1. What is a "class"? When and why do we use them?
2. What are some examples of classes that you've used before?
3. What is a constructor method?

## Practice
1. Create a ComplexNumber class with a constructor method.
2. Write methods for addition, subtraction, multiplication, and division with objects of your ComplexNumber class.
3. Write a __str__ method for your class. What is special about this method? What is the difference between your __str__ method and the default one for your class?

## Application
Design a DataFrame class to store generic tabular data. Consider how your constructor method should work. What other methods should your class have (or in other words, what other operations do you want to be able to perform on a generic data set)? Implement your class.

