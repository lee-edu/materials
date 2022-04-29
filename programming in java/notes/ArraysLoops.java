public class ArraysLoops {

  static int countTarget(String[] strs, String target) {
    int count = 0;
    for (int i = 0; i < strs.length; i++) {
      if (strs[i].equals(target)) {
        count++;
      }
    }
    System.out.println(count);
    return count + 5;
  }

  public static void main(String[] args) {
    String[] fruits = { "apple", "banana", "cherry", "apple", "apple", "banana" };


    assert countTarget(fruits, "apple") == 3 : "Error apple 3"; // 3
    countTarget(fruits, "pear"); // 0
    countTarget(new String[]{"banana", "banana", ""}, "banana"); // 2

    /*
    int[] nums = { 8, 9, 10, 23 };
    sum(nums); // 50
    sum(new int[] { 10, 10, 10 }); // 30
    sum(new int[] { 8, 1 }); // 9

    average(nums); // 12.5
    average(new int[] {1,2,3,4,5}); // 3.0
    */
  }
}
