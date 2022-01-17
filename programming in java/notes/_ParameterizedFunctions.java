class ParameterizedFunctions {


  static void sayHiTo(String name){
    /*

    */
    System.out.println("Hello " + name);
  }

  static int addOne(int x){
    /*
      A parameter is a variable that stores the input when called
      It has to have a type and a name
      It goes in the parenthese after the name of the function
    */

    /*
      Returns have 2 parts:
      1) the type of the thing being returned
      2) the thing being returned
      In this example, the type is int
      and x+1 is being returned

      A function can only return ONE thing
    */
    return x + 1;
  }

  // Write a function that takes a number
  // and returns the number squared
  // 276^2 = ?
  static int squareNumber(int x){
    return x * x;
    // return x * x;
  }


  static void sayHi(){
    System.out.println("Hello");
    /*
      Printing is different from returning
      You can print more than once in a function
      but you can only return once
    */
    /*
      A function RETURNS something IF AND ONLY IF
      you see the word return
      Otherwise it is void and returns nothing
    */
  }

  static int subtract(int x, int y){
    return x - y;
  }

  public static void main(String[] args) {
    // Holds all the main code
    // Basically what the program does when you run it

    // Functions have two parts
    // First, define it (above)
    // Then you can call it


    /*
    We pass in 3 as a parameter to the addOne function
    The function returns the int 4
    The int 4 is stored in a variable named answer
    Then answer is printed
    */
    int answer = addOne(3);
    System.out.println(answer);

    answer = squareNumber(276);
    System.out.println(answer);

    subtract(10,5); // returns 5
    subtract(5,10); // returns -5
  }
}