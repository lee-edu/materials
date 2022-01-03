import java.util.Scanner;
public class Functions {

    // Global variables here
    // A global variable can be used in any function
    static Scanner sc = new Scanner(System.in);
    static int x = 5;

    /**
     * A function is a way to bundle code together
     * Two parts:
     * 1) Define the function
     *  outside the main but inside the class
     * 2) Call the function
     */

    // Part 1: I defined a new function called nameOfFunction
    public static void nameOfFunction(){
        sc.nextLine();
        System.out.println("Part 1 of code");
        System.out.println("Part 2 of code");
        System.out.println("Part 3 of code");
    }

    public static void gameOver(){
        x = 3;
        System.out.println("The game is over!");
    }

    public static String yesOrNo(){
        String ans = sc.nextLine();
        if (ans.equals("yes")){
            return "yes";
        }
    }

    public static void main(String[] args) {
        // Part 2: Call the function
        nameOfFunction();
        nameOfFunction();
        nameOfFunction();

        String ans = yesOrNo();

        // Example of using functions
        if (ranAway){
            escapedTheCave();
            gameOver();
        }else{
            stuckInCave();
        }

        if (died){
            gameOver();
        }
    }
}
