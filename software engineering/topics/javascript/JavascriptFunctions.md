# First Class Functions
In Javascript, functions are considered **first-class**; in other words, they are treated just like any other variable. For example, the following two snippets of code are exactly the same:
```js
// Snippet 1
const foo = function(x) { return x + 1; }

// Snippet 2
function foo(x) {
  return x + 1;
}
```

This allows us to write functions that can take functions as parameters, or even return functions. These are called **higher-order** functions.

You can read more about this concept [at the Mozilla developer docs](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)!

1. Examine the following snippet of code. What is printed at the end?
```js
const add1 = function(x) { return x + 1; }
const add2 = function(x) { return x + 2; }
const foo = function(fn1, fn2, x) {
  return fn1(fn2(x));
}

console.log(foo(add1, add2, 3));
```
2. Write a function `addN` that takes a number `n` and returns another function that takes a number `x` and returns `x+n`. For example, calling `addN(2)(3)` should return 5.

# Arrow Functions
There is also another way to write a function in Javascript. For the most part, you can treat this as syntactic sugar; notice the lack of the `return` statement. The following three lines of code each do the exact same thing:
```js
function foo(x,y) { return x + y; }
const foo = function(x,y) { return x + y; }
const foo = (x,y) => x + y;
```

The only difference is that in arrow functions, the keyword `this` refers to the **parent scope**.

## Currying
Arrow functions allow us to do something called **currying**, which means to continually define one-parameter functions. Examine the following snippet of code:
```js
const mul = x => y => z => x * y * z;
const mul2 = mul(2);
const mul6 = mul(2)(3);
```

1. Write an arrow function that takes a string and returns the lowercase version of that string.
2. Write an arrow function that takes a string `prefix` and returns another function that prepends `prefix` to its parameter.
3. Write an arrow function that takes a string `prefix` and returns a function that takes a string `postfix` that returns another function that takes a string and returns correctly prepends/appends the pre/postfix to its parameter.
4. Write the curried version of the following function:
   ```js
   function add(x) {
     return function(y) {
       return function(z) {
         return x + y + z;
       }
     }
   }
   ```
     1. Use the above definition to create functions so that this code would run without error: `add2(5)(3) == add7(3)`

# Practice
These practice questions are taken from [eloquentjavascript.net](https://eloquentjavascript.net/05_higher_order.html).

1. Write a higher-order function `loop` that provides something like a for loop statement. It takes a value, a test function, an update function, and a body function. Each iteration, it first runs the test function on the current loop value and stops if that returns false. Then it calls the body function, giving it the current value. Finally, it calls the update function to create a new value and starts from the beginning.  
When defining the function, you can use a regular loop to do the actual looping.  
For example, `loop()
1. Write a function `every(array,test)` that returns whether `test` returns true for every element in the given array.