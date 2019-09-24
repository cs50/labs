# For Loop

In this lab you will learn:

- Why we have a for loop
- How to use a for loop

## What is a For Loop?

The **for loop** is probably the most frequently used loop of the three types of loops. It is very useful when we want to repeat something a known number of times.

Eventually we'll see how for loops can be useful for:
* Repeating a block of code 10 or 20 or *n* times when you know in advance the value of *n*
* Accessing each individual character in a string
* Looking at each element in an array (more on this to come later!)

Let's start by taking a look at the analogous loop in Scratch.

{% next %}

![scratch_repeat](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/forloop/repeat.png)

can be recreated in C by:

```c
for (int i = 0; i < 50; i++)
{
    printf("hello, world\n");
}
```

A for loop has three parts (included in parentheses after the word for, and separated by semicolons)

* **Initialization**: `int i = 0` is an initialization of the `int` variable `i`, which means that we created a variable and set its initial value to 0. `i` is a conventional name for a counting variable that keeps track of how many iterations of the loop we’ve already done.

* **Loop Condition**:  Then `i < 50` is the Boolean expression that the for loop checks, to determine if it will continue or not. When this condition is true, the for loop will run the code inside the curly braces. And since we started `i` at 0, stopping before `i` reaches 50 will mean this runs exactly 50 times, as we intended.

* **Increment Statement**:  The third part is the loop modification. This code is executed at the end of every loop. In this case, we increase the value of `i` by 1. As soon as `i` is no longer less than 50, the condition fails and the loop will end. The end result is that `hello world\n` is displayed exactly 50 times.

{% next %}

By taking advantage of loop modification, you can also get a loop to do something slightly different each time the loop repeats, or iterates.

For example, let's look at the following code:

```c
for (int j = 1; j <= 10; j++)
{
    printf("%i\n", j);
}
```

Here we start our counting variable, `j`, at 1 and execute the loop until `j` is no longer less than or equal to 10. Our first execution of the loop prints 1 on its own line. We then increment `j` by 1 and check the condition to see if it's still true. Since `j` is now 2, it's true that `2 <= 10` so the loop repeats printing 2 on it's own line. This continues until we've printed out the count from 1 to 10 inclusive.

{% next %}

## Your Turn

Modify the code on the right to add up the numbers from 1 to 10, using either the supplied for loop or creating your own. Store the total in the variable named `total`.

{% spoiler "Hint" %}

Keep in mind that you can use the value of `i` in your calculation. You can also change the loop so start at one and end when `i <= 10`. This gives you a value which can be added to `total` during each iteration.

{% endspoiler %}

[For more info, download the CS50 Loops Reference Sheet](https://ap.cs50.school/assets/pdfs/unit1/loops.pdf)
