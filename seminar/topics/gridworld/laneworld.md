# LaneWorld
Our next project will be based on the game [Super Auto Pets](https://teamwoodgames.com/).

Take some time to play a few rounds and answer the following questions:
  1. What happens each "step"?
  2. How does a player win a round?
  3. What attribute does each pet have?
  4. How do different pets differ from each other?
  5. What resources limit your team options?

## Implementation
We will be using GridWorld to code a similar engine. This time, in addition to extending the `Actor` class, we will also be extending the `ActorWorld` class. The Pets will be placed on a `1x10` Grid (which we will call a Lane).

### The Actors
  1. Write a `Pet` class that extends `Actor`. It should be capable of doing all actions as described above.
  2. Design **5** different extensions of `Pet`. Try to come up with something original! **Do not write the code (yet).** Use the index cards to describe what the Pet should be able to do. Try to be as detailed as possible, as if you were writing documentation!
  3. After swapping index cards, write the code for the 3 designs that you received!
  4. TEST YOUR ACTORS! In your Runner, instead of creating a World, run some tests using `Scanner` and terminal.

### The World
  1. What does `setMessage()` in `World` do?
  2. What information would you need to display via `setMessage` for LaneWorld?
  3. When and how often should that information be updated?
  4. Write a `LaneWorld` class that extends `ActorWorld`. It should take two `ArrayList<Pet>`s (team A and team B), and place them in the `1x10` world accordingly. Override the `step` method so that:
     - The Pets act in the same way as Super Auto Pets
     - The message is updated to reflect what is happening.

> You can use `System.out.println()` to help debug!