public class WhileLoopNotes {
	public static void main(String[] args){

		// While Loops
		boolean gameOver = false;
		int i = 0;
		// Runs until the condition is false
		while (!gameOver){
			System.out.println("Play game");
			if (i > 10){
				gameOver = true;
			}
			i++; // Short for i = i + 1
		}

		// Template
		// Get their input once
		// While they have not typed "A" or "B"
		// Get their input again

		while (???){ // Try to figure this out
			???
		}

		// Here we are guaranteed that 
		// input is either "A" or "B"
	}
}