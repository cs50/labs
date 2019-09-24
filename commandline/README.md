# Command-Line Interaction

In this lab you will learn:

- What are command-line arguments
- How can we use command-line arguments
- Why we need to test for the correct argument count

## What are Command-Line Arguments?

Up until now, we've been getting user input through using functions such as `get_int()`, `get_string()`, etc. There is another way of getting input, which is by using **command-line arguments**.

<img src="https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/commandline/command_line_interaction.gif" width="400">

Above you'll see two implementations of hello; one prompting the user with `get_string()` and the other using command-line arguments.

We would execute `hello0.c` it by typing `./hello0`.

But we would execute `hello1.c`, by typing `./hello1 David`.

{% next %}

## How Do We Use Command-Line Arguments?

In order to allow our program to accept command-line arguments, we revise our `main` function to include the input arguments `argc`, an integer and `argv`, an array of strings:

```c
int main(int argc, string argv[])
```

The first of these arguments, `argc` stands for argument count, and represents the number of arguments passed through the command line. Each word typed at the command line is considered an argument, where the first is the name of the program we are calling. Previously, we wrote our `main`function to take no arguments by using `void`.

For instance `./hello0` has an argument count of one, while `./hello1 David` has an argument count of two.

The second argument, `argv`, stands for argument vector, and is the actual array representing the arguments themselves. Each value in the array is a string.

<img src="https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/commandline/argc2.png" width="350">

{% next %}

## Why Check for Argument Count?

Let's see what happens if we execute our new program, `hello1` without typing in any command-line arguments.

<img src="https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/commandline/hello_null.gif" width="400">

Why are we getting `hello (null)`? What is (null)?

Since our program, `hello1`, was expecting the name to be input at the command line, we ended up with

<img src="https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/commandline/argc1.png" width="350">

The program is printing the value `argv[1]` after `hello,`, but `argv[1`] is an empty string, or `null`.

Expecting command-line input and not receiving it can produce unpredictable results, or even make our program crash.

This is why we always check that the correct number of arguments are input at the command line before executing our program.

{% next %}

## How to Check for `argc`

When using **command-line arguments** it's always a good idea to include a check for the correct argument count at the top of our program, certainly before trying to access any elements in the `argv` array.

For a program that requires one argument after the program name, where `argc` is expected to be 2, this could look like:

```c
if (argc != 2)
{
    printf("Incorrect number of arguments!\n");
}
else
{
    // program continues here...
}
```

## Your Turn

The program on the right uses `get_string()` to get user input. Edit the program to accept command-line arguments then check that the argument count is correct (accept one argument entered after the program name for an argument count of 2). Finally, print out `hello, ` followed by the value of `argv[1]`.

{% spoiler "Need a hint? %}

1. Modify the main function to `int main(int argc, string argv[])`
1. Check that the argument count is correct (`argc` should equal 2, meaning there is one argument at the command line after the program name)
    1. If `argc != 2` print an error message
    1. Else print out `hello, ` followed by `argv[1]`

{% endspoiler %}  

Remember to compile your program and test it. Be sure to test for all cases: with one command-line argument after calling the program name, with more than one argument, and with no arguments.

[For more info, download the CS50 Command-Line Interaction Reference Sheet](https://ap.cs50.school/assets/pdfs/unit2/command-line_interaction.pdf)
