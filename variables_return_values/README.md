# Variables, Return Values

Whereas some functions take input (e.g., `print`), others produce output. And some do both!

For instance, recall that Python has a function called `input`, which waits for the user to type something in the terminal window, followed by Enter, and then "returns" whatever the user typed so that it can be stored in a variable (or even passed as input to another function).

In `input.py` in the text editor at top-right, write a program that

1. prompts a user, via `input`, for his or her name, and
1. prints precisely `hello, name`, where `name` is the user's inputted name.

{% check %}

{% next %}

It turns out that `input` itself also takes input, an optional argument that tells `input` with what message to prompt the user for input. For instance, if you call

```
s = input()
```

in a program, without an argument to `input`, all the user will see is a blinking prompt, implicitly indicating that the program is waiting for input. (Not very obvious!) If you instead call

```
s = input("Name: ")
```

in a program, with an argument to `input`, the user will instead see that argument (i.e., `Name: `) followed by a blinking prompt. (More obvious!)

Modify `input.py` in the text editor at top-right in such a way that the program

1. prompts a user, via `input`, for his or her name explicitly (as with `Name: `), and
2. prints precisely `hello, name`, where `name` is the user's inputted name.

{% check %}

{% submit %}
