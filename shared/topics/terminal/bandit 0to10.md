# Bandit
**Make sure your team saves the passwords for each level!**

Once you are in Bandit, you can proceed to the next level by typing `ssh bandit[LEVEL#]@localhost` instead of the entire url for bandit. (example: `ssh bandit3@localhost`)

## Model A | Levels 0 to 5
1. What does `ssh` do?
1. What is a **port**, and how do you specify a port when using `ssh`?
1. Write the command to `ssh`:
    1. into user `spy` on port `33501` of server `secret.server`
    1. into user `agent` on port `2234` of server `secret.server`
    1. into `public.server`
1. What does `localhost` refer to?
1. What does `localhost:8080` refer to?
1. What does `cat -` do? In other words, what does `-` represent when it is used as a parameter for `cat`?
1. What is the difference between `cat Secret Password File` and `cat "Secret Password File"`?
1. What does it mean to **escape** a character?
1. Write the command to `cat` the file named `Secret Password File` *without* using quotes (`"`).
1. Write a string that contains two words separated by a tab and ends with a newline. Use **escape characters**.
1. How do you list all files and folders in a directory, even if they are hidden?
1. What is **ASCII**?
1. Explain the syntax and usage of the `file` command.
1. How do you use **wildcards** in a terminal command?

### **STOP** HERE. The **presenter** should check in with the teacher.

## Model B | Levels 6 to 10
1. Explain the syntax and usage of the `find` command.
1. Write the command to `find`:
    1. all `.jpg` files in my current directory
    1. all files or folders owned by the user `root` in my current directory
    1. all files named `file.hidden` on my computer
1. On `bandit5`, write the command to print the file types of *all* files in `inhere`.
1. What are **file permissions**, and what are they used for?
1. Explain the usage of `chmod`.
1. Convert the following binary numbers to decimal.
    1. `111`
    1. `101`
    1. `001`
1. Each of the following is the permission output of `ls`. Explain what they mean, and convert them to the chmod numerical format.
    1. `drwxrwxrwx`
    1. `-rw-r--r--`
    1. `-rwxwrx---`
    1. `drwxr-x---`
1. Explain each permission and convert them to the `ls` format.
    1. `777`
    1. `217`
    1. `646`
1. Does `echo "Hello" > world.txt` use **piping** or **redirection**?
1. Explain the usage and syntax of `strings`.
1. True/False: `strings` only works on `txt` files.
1. Write the terminal commands to:
    1. Output all lines in `big.csv` that contain the phrase `pharma`
    1. Output all lines in `small.csv` that don't contain the phrase `pharma`
    1. Output all the lines in `medium.csv` that contain at least one `M`
    1. Output the results of running `program.py` into `results.txt`
    1. Output the results of running `another_program.py` into `log.txt`, but only if the line contains `LOG:`

### **STOP** HERE. The **presenter** should check in with the teacher.