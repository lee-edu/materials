/**
 * Ask a multiple choice question,
 * then let the game branch off depending
 * on how the player responds.
 */
System.out.println("QUESTION");
String answer = sc.nextLine();
if (answer.equals("A")){
	// Code A
}else if (answer.equals("Option B")) {
	// Code B
}else if (answer.contains("Y")){ // Check for the letter Y
	// Code C
}else{
	// Code D
}

/**
 * Do this to clean up your code!
 */
// Command+Shift+P
// Format Document


/**
 * You can bundle code together by
 * _defining_ a function. Then, you can
 * _call_ that function as many times
 * as you want!
 */

// Define the function _outside your main_
// but _inside the class_
public static void sayHello(){
    System.out.println("Hello!");
}

// Call the function _inside your main__
sayHello();

// You can call it as many times as you want!
sayHello();
sayHello();
sayHello();