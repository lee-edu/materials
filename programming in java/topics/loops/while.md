# While Loops
Computers are GREAT at doing something over and over again! If we want code to repeat, we use something called a **loop**.

Part of this worksheet is adapted from Helen Hu's CS POGIL work.


## Model A - Useful Assignments
Evaluate these assignments *manually*, without using a Java shell.
```java
int x, y, z, a;

// Section 1
x = 1;
y = 2;
y = x;
x = y;    // 1. What are the values of x and y now?

// Section 2
x = 1;
y = 2;
z = y;
y = x;
x = z;    // 2. What are the values of x and y now?

// Section 3
z = 2;
z += 1;
z += 1;
a += 1;   // 3. What are the values of z and a now?
```

4. Why is the value of `x` not 2 at the end of section 1?
5. What happens to the values of `x` and `y` in section 2?
6. What is the purpose of `z` in section 2?
7. Why is it possible to **increment** (increase by one) `z` but not `a` in section 3?

## Model B - While Loops
```java
int i = 0;
while (i < 3){
  System.out.println(i);
  i += 1;
}
System.out.println("Task completed.");
```
1. Examine the code for a **while** loop, along with the corresponding diagram. Which line of code increments `i`?
2. What happens to the value of `i` in the **body** of the loop?
3. Will this program print the number `3`? Why or why not?
4. How many times will this loop run? Explain your reasoning.
5. Suppose the body is reversed:  
    ```java
    while (i < 3){
      i += 1;
      System.out.println(i);
    }
    ```
   1. How does this change what prints?
   2. Does this change the *number* of times the program prints?
6. What are *three* different ways to modify the code so that the loop only executes _twice_?
7. What are the three parts of a whileloop that controls the number of times it executes?
8. What would happen if we deleted the increment statement in the body?
9. What syntax tells you where the body of the while loop starts and ends?

## Practice
1. Write a loop that prints all the _even_ numbers from 0 to 100 (inclusive).
2. Write a loop that prints all the _odd_ numbers in [0,100].
3. Write a loop that prints all the multiples of 50 in [0,500].