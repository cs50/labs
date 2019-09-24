# While Loop

In this lab you will learn:

- What is a while loop
- How and when to use while loops

## What is a While Loop?

As we'll soon see, there are three types of loops we can use in C. While each type of loop can be made to do just about anything, each type of loop serves a particular purpose.

The **while loop** repeatedly executes a block of code as long as the condition evaluates to true. We usually use a while loop when we don't know in advance how many times we want a block of code to repeat. An example might be to determine the number of times a number can be divided by 2:

```c
int n = get_int("Enter a number: ");
int counter = 0;

while (n > 1)
{
    n = n / 2;
    counter++;
}

printf("Your number can be divided by 2 %i times\n", counter);
```

{% next %}

The syntax for a while loop is similar to the if statement, with the key word `while` replacing the `if`, where the condition is in parentheses and the block of code to execute is wrapped inside of curly braces `{}`. But don't confuse the `while` loop with an `if` statement. Though the syntax is similar, the execution is different. The `while` loop repeatedly executes the block of code while the condition is true. The `if` statement executes the block of code once if the condition is true.

## Forever Loop

In Scratch, we saw a **forever loop** which was useful when we wanted to repeat an action forever:

![if_x_y](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/whileloop/forever.png)

We can use the while loop in C to create a forever loop:

```c
while (true)
{
    printf("hello, world\n");
}
```

Since the `while` keyword requires a condition, we use `true` as the Boolean expression to ensure that our loop will run forever. Our program will check whether the expression evaluates to true (which it always will in this case), and then run the lines inside the curly braces. Then it will repeat infinitely until we explicitly tell the program to break out of it.

{% next %}

## Your Turn

Complete the program on the right to create a loop that determines how many times you can double a number before it reaches 100.

Then test your code, as you did in previous labs, with valid inputs, invalid inputs and corner cases. One corner case you might try is an input of zero. What do you think will happen?

{% spoiler "Does your program seem to hang?" %}

When you enter a zero for input, you can double that number forever, and the result is still zero! So the condition you wrote is most likely always going to be true! Because of this, your loop acts as a forever loop and continues to run, giving the appearance of your program hanging. You can stop your program from executing by holding down `ctrl + c`.

{% endspoiler %}

What happens when you enter a negative number?
{% spoiler "Not sure what the strange error message means?" %}

You'll probably see something like:
```
runtime error: signed integer overflow: -2147483648 * 2 cannot be represented in type 'int'
```

Since it's possible that if the condition your wrote is something like (n < 50) that it will always be true, since a negative number times two always results in a negative number. Therefore, the loop will continue as long as it can.

Also, remember that the smallest value that an int can hold is -2<sup>31</sup> which is -2147483648, so when we try to store a value smaller than this, we end up with an **integer overflow** error, which is what this message is telling you.

{% endspoiler %}

[For more info on loops, download the CS50 Loops Sheet](https://ap.cs50.school/assets/pdfs/unit1/loops.pdf)
