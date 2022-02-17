# Review              <span>Name:</span>
## Objectives
Review the following topics:
  - declaring, assigning, and initializing variables
  - different variable types
  - conditional statements

## Variables
1. Write the line of code that will:
   1. Declare a new `int` variable named `x` without assigning any value
   2. Initialize a new `String` variable to have the value `"Happy New Year!"`
   3. Reassign an existing variable `year` to have the value `2022`
2. What is the difference between initializing and reassigning a variable?
3. In terms of computer memory, what happens when you declare a new variable?
4. What type of variable is best suited for:
   1. Counting votes
   2. Speed of a bus
   3. Name of a park
   4. Checking if a light is on

## Conditionals
5. Let `p = true` and `q = false`. Evaluate the following statements:
   1. `p && q`
   2. `!(p||q)`
   3. `p && (q || !q)`
6. Let `x = 3, y = 4, z = 5`. Evaluate the following statements:
   1. `x <= y`
   2. `z > 12`
   3. `x > y || z <= 6`
7. Let `a = 3, b = 4, c = 5, d = true`.  
```java
if (!d || a < c || (b > 1 || !d) && d){
  d = !d;
  System.out.println("Case 1");
} else {
  d = true;
  System.out.println("Case 2");
}
```
   1. What will be the value of `d` after this code is executed?
   2. What will be printed out if the code is executed again with `d` set to the new value?