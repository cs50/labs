# Do-While Loop

In this lab you will learn:

- What is the difference between a while and do-while loop
- How and when to use do-while loops

## What is a Do-While Loop?

The **do-while loop** is similar to a while loop in the sense that it repeatedly executes a block of code as long as the condition we give it is true. The do-while loop though, will always execute at least once, and then check the condition to determine if it should execute again and again.

This is very useful when we want to validate user input. For instance, say we want to prompt the user for a positive integer, and we don't want to accept negative numbers or zero. The CS50 `get_int()` function does a great job at rejecting inputs that are not `int`s, but since negative numbers and zero are `int`s, we have to do our own checking for these:

```c
int positive_int;

do
{
  positive_int = get_int("Enter a positive int: ");
}
while (positive_int <= 0);
```

{% next %}

The condition here often seems counterintuitive. We want to accept a positive number, yet the Boolean expression checks for negative numbers and zero. However, the idea here is that we want to repeat the prompt when the input is invalid. And our input is invalid when `(positive_int <= 0)` is true.

Note that we are declaring our variable, `positive_int`, outside of our loop. We do this because we may want to use this variable later. A variable declared in a loop has a scope limited to the curly braces that surround it, meaning its value is only available inside the loop. 

Note also that there is a semicolon `;` after the condition, since this is the end of our do-while statement.

{% next %}

## Your Turn

Complete the program to the right to include a do-while loop to validate user input. The program should only accept a number between 1 and 10 inclusive.

Be sure to test your program with numbers in this range, numbers outside of this range, as well as zero, 10, negative numbers and floating point numbers.

You may have to use a logical operator, such as `&&` (AND) or `||` (OR) to combine two conditions for this.

[For more info on loops, download the CS50 Loops Sheet](https://ap.cs50.school/assets/pdfs/unit1/loops.pdf)
