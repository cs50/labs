# Operators

In this lab you will learn:

- How math operators work in C
- How and when to use the remainder operator
- The different ways of using assignment operators

## Arithmetic Operators

The addition (`+`), subtraction (`-`), and multiplication (`*`) **operators** work the same way in C as they do in your math class. No big surprises here.

We can write `10 * 3` and of course the result would be *30*.

We can use these operators with numbers or variables. If we've already assigned the value *10* to an integer variable `a`, we would get the same result by writing:

```c
a * 3;
```

{% next %}

However, this is not storing the resulting value of *30* in anything. The value of `a` is not changed. Its value is just used as part of this calculation.

If we wanted to store the result of this calculation in a new integer variable, `b`, we could write:

```c
int b = a * 3;
```

In order to change the value of `a` to be equal to 3 times itself, our code could look as follows:

```c
a = a * 3;
```

Notice that we didn't write `int` in front of the `a` in this last example. Why? Well in order for `a` to already have a value, `a` would have already been declared earlier in our program!

{% next %}

## What about division?

You'll notice that division wasn't mentioned in the section above. The symbol used for division is `/`, however, division in C works differently when we are dividing `int`s than the division we learned in grade school.

If we write:

```c
5 / 2;
```

we are telling our program to divide two `int`s. Now remember from our earlier labs, ints can only hold whole numbers. So the operation of dividing two `int`s will truncate, or cut off everything in the result that comes after the decimal point. The result of this operation is therefore 2!

If doesn't matter if we try to store this in an `int` or a `float`. The result of the operation will be evaluated first, and then assigned to my variable.

If we wanted to save the output of this calculation:

```c
int a = 5 / 2;
```

the value of our `int` `a` will be 2.

{% next %}

If we save the output of this calculation to a `float`:

```c
float b = 5 / 2;
```

the value of `b` will still be 2.0.

When at least one of the numbers in our division statement is a `float`, C will interpret this as dividing two `float`s. Floats are variables that can hold a number with a decimal. So:

```c
float b = 5.0 / 2;
```

will assign 2.5 to `b`.


Now if we write:

```c
int a = 5.0 / 2;
```

let's think about what happens. The division results in a `float`, but now this value is assigned to an `int`, so again, everything after the decimal point gets truncated, so `a` gets the value 2.

{% next %}

# Modulo

An operator in most programming languages that you may not have seen before, is the remainder, or **modulo** operator. The symbol used by modulo is the `%` sign, and an operation using modulo looks like this:

```c
int remainder = 5 % 2;
```

Since 2 goes into 5 twice with a remainder of one, `remainder` gets 1.

Though it may not be obvious at first, this operator can be very useful in programming. It can tell you if a value is divisible by a number, and as we'll see later can be used as a wrap around operator, where numbers wrap around back to zero after reaching a certain value.

Modulo can only be used with `int`s.

{% next %}

## Assignment Operators

We've already seen the assignment operator `=`. This evaluates the expression on the right side of the statement, and assigns it to the variable on the left.

There are a few shortcuts for assignment that you'll soon encounter as well.

| Symbol     | Example      | Result |
| ------------- |------------------| ------- |
| `++`           | `a++;`    | increases the value of `a` by 1
| `--`         | `a--;`   | decreases the value of `a` by 1
| `+=`           | `a += 2;`           | sets `a` to 2 plus the initial value of `a`|
| `-=`           | `a -= 2;`           | sets `a` to 2 minus the initial value of `a`|
| `*=`          | `a *= 2;`            | sets `a` to 2 times the initial value of `a`|
| `\=`          | `a \= 2;`            | sets `a` to 2 **divided by** the initial value of `a`|


{% next %}

## Your turn!

The program on the right is partially completed. It asks for user input and assigns it to an int variable a. Your job is to declare additional variables, as per the comments, and use the appropriate operator to assign it the proper value.

<!--
{% spoiler "Doug's video on operators" %}
{% video https://www.youtube.com/watch?v=f1xZf4iJDWE %}
Note: Boolean operators will be discussed in the Boolean Expressions Lab.
{% endspoiler %}
-->

[Download the CS50 Operators Reference Sheet on Operators](https://ap.cs50.school/assets/pdfs/unit1/operators.pdf)
