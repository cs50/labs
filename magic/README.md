# Magic Numbers

In this lab you will learn:

- What we mean by magic numbers
- Why magic numbers are considered poor design

## What are Magic Numbers?

In the variable lab, we replaced a hard-coded number representing age with a variable. This was a far better design than having to change the program each time we run it to hard-code another value.

```c
// My age next year
printf("Next year I'll be %i years old.\n", 17 + 1);

// My age in 10 years
printf("In 10 years, I'll be %i!\n", 17 + 10);

// My age in 50 years!
printf("In 50 years, I'll be %i! Wow!\n", 17 + 50);
```

However, there are still other numbers directly written into the program, even after replacing 17 with the variable `age`. We still have a 1, 10 and 50. If we didn't have comments, would we know what these numbers represent? While this is a simple program and it may be easy to understand what each calculation is doing, in more complex programs the meaning of hard-coded numbers may not be as obvious.

Numbers that are directly written into our code in this way are sometimes referred to as **magic numbers**.

{% next %}

## Using Constants Instead!

When we have a need to use a number in a program whose value is never going to change, it's considered good design to use a constant.

Let's take an example. What if we wrote a program that uses the number 3.14. Some people might recognize this as Pi, but others may not be sure what this number represents.

To improve the readability of our code, we could define Pi as a constant.

A program with Pi defined as a constant could look like this:

```c
#include <cs50.h>
#include <stdio.h>

#define PI 3.14

int main(void)
{
    float radius = get_float("Radius in inches: ");
    float area = PI * radius * radius;
    printf("Your area is %.1f square inches.\n", area);
}
```

Notice the syntax for creating the constant Pi, is the keyword `#define` then the name of the constant, `PI`, followed by the replacement value, 3.14. We write `#define` statements before the `main` function. The name of the constant is, by convention, all caps.

The general syntax to create constants is:

```
#define NAME <replacement value>
```

By defining these values once, at the top of our program, it becomes easier to change these universal values when necessary. Say for instance, we need a program above to calculate more accurately with `PI`, we can easily change 3.14 to 3.14159265. If we had multiple occurrences of `PI` in our program, each of these would reflect the more accurate value.

{% next %}

## Your Turn

Modify the program on the right (the same program as in the variables lab) and change each of the **magic numbers** to **constants**. The first of these is already done for you.

Be sure to compile your program by typing:

```
make magic
```

and then test it several times by executing:

```
./magic
```

Finally when all seems good, check your style with:

```
style50 magic.c
```
