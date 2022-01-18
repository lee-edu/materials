# GridWorld
GridWorld is a graphical environment that helps visualize the behavior of objects. It was used in the CS AP exams, but we will be taking it in another direction. [You can read more on the GridWorld website.](https://horstmann.com/gridworld/gridworld-manual.html)

## Setup
Clone [this repository]() and open the GridGames folder with VS Code. It should open as a Java project. If it does not, make sure you have the **Extension Pack for Java** installed. You might also have to first open a `.java` file, which can be found in the `projects` directory.

The `gridWorld` directory contains the base source code for GridWorld. **Do not edit any files in this directory!** It is purely for reference.

You will be working in the `projects` directory. Browse through the existing projects. Also notice that in `.vscode/settings.json`, each project folder has been added. This is required in order to run the projects through VS Code.

Run `BugRunner.java` in `firstProject`. A GUI (Graphical User Interface) should appear. Figure out what the `Step`, `Run`, and `Stop` buttons do. Try changing the slider as well from `Slow` to `Fast`.

## GridWorld Basics
This section is pulled from the [CollegeBoard GridWorld Student Manual](https://secure-media.collegeboard.org/apc/GridWorld_Case_Study_Student_Manual_with_Appendixes_Aug_2007_updated.pdf). Feel free to flip through this document!

To answer the following questions, looking at the source code in `gridWorld` as well as the classes in `boxBug` and `critters` will be very helpful.

1. What happens when the bug is at an edge of the grid?
2. What happens when a bug has a rock in the location immediately in front of it?
3. Does a flower move?
4. What behavior(s) does a rock have?
5. Can more than one Actor be in the same location in the grid at the same time?
6. What does 0 degrees correspond to for `setDirection`? What about 180?
7. What does the `turn` method do?
8. Why is the `turn` method called _twice_ in the `BoxBug` class?
9. Why can the `move` method be called in the `BoxBug` class even though it is not defined in the code? (_Hint:_ `extends`)
10. What is the purpose of the `steps` property in `BoxBug`?
11. What is the purpose of a `Runner` class?

## Problem Set #1: Fancy Bugs
Create a project named `fancyBugs`. Be sure to add it to the source path as well so you can run the project via VS Code. The runner class should instantiate an **Unbounded** `ActorWorld` that spawns the following bugs. The bugs should behave as described.

1. `CircleBug` is identical to BoxBug but only `turn`s once instead of twice.
2. `SpiralBug` drops flowers in a spiral pattern. _Hint:_ Adjust `sideLength` when it turns.
3. `ZBug` moves in a Z pattern, starting in the top left corner. After completing one "Z", a `ZBug` should stop moving. If in any instance, it can't move, it will stop forever. `ZBug` should take the length of the "Z" as a parameter in the constructor.
4. `RectangleBug` takes two parameters in its constructor: `l` and `w`; it should draw a rectangle with length `l` and width `w`.
5. `RandomBug` moves and turns randomly with each step.
6. `RainbowBug` does not move but changes color each time it acts; it rotates between red, orange, yellow, green, and blue.
7. `PolygonBug` takes two parameters in its constructor: `n` and `s`; it should draw a regular `n`-gon that has sides of length `s`.

