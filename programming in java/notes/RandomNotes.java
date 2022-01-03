import java.util.Random;

public class RandomNotes {
  // Make a new global random generator
  static Random r = new Random();

  public static void main(String[] args) {

    // Generate a random number from [0, n]
    int n = 30;
    int randomNumber = r.nextInt(n);
    System.out.println(randomNumber);

    // Has 80 percent chance of printing
    if (r.nextInt(100) < 80) {
      System.out.println("Hello world.");
    } else {
      System.out.println("Goodbye world.");
    }
  }
}