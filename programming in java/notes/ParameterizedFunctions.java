public class ParameterizedFunctions {

  /*
    Example of a void function
    Void means there is no return value

    `Print` and `return` are different
    You can print as many times as you want
    but you can only return ONCE

    A function RETURNS something IF AND ONLY IF
    you see the word return
    Otherwise it is void and returns nothing
  */
  static void sayHi(){
    System.out.println("Hello.");
  }

  /*
  f(x) = x + 1
  A parameter is a variable that represents the function input
  It goes in the parentheses after the name of the function

  The return value is the output
  It has two parts:
  1) the type of the thing being returned
  2) the thing being returned

  In this example, the type is int
  and x + 1 is being returned

  A function can only return ONE thing
  */
  static int addOne(int x){
    return x + 1;
  }

  /*
    A function can have multiple parameters;
    just separate them with commas!
  */
  static int subtract(int x, int y){
    return x - y;
  }

  // Write a function that takes a number
  // and returns the number squared
  // Use your function to find 276^2
  static int square(int x){
    return x * x;
  }

  public static void main(String[] args) {
    /*
      The main function is the main thing that runs
      Only code in the main function will run
    */

    /*
      To call a function, write its name and ()
    */
    sayHi();

    // This doesn't print anything! Why?
    square(276);

    /*
      We declare a new int variable named answer
      We assign the value `square(276)` to answer
      We pass 276 as x into the function named square
      and the return value is stored in the variable
      Then we print what is stored in the variable answer
    */

    int answer = square(276);
    System.out.println(answer);

    // The order matters when you call the function
    subtract(10,5); // 10 - 5 >>> 5
    subtract(5,10); // 5 - 10 >>> -5
  }
}