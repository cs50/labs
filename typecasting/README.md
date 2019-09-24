# Typecasting

In this lab you will learn about:

- What we mean by typecasting
- Possible uses of typecasting
- Implicit vs. explicit typecasting

## What We Mean By Typecasting

As we know by now, there are several data types in C: `int`s, `float`s, `char`s, etc. There are situations when we might want to convert a variable from one data type to another data type; we can do this using **typecasting**, or just **casting**.

Why would we want to **cast** a variable from one data type to another? Say we we want to write a program to calculate the average class size at our school. We have two integer variables: the sum of class sizes, `class_size_total`, and the total number of class, `total_classes`.

```c
int class_size_total = get_int("Sum of class sizes: ");
int total_classes = get_int("Number of classes: ");
```

If we calculate the average as:

```c
float average = class_size_total / total_classes;
```

What kind of result can we expect?

{% next %}

Remember, when we divide an `int` by another `int`, C truncates any values after the decimal point. If we want to get a more precise value here, we can **cast** one of our `int` variables to a `float` to calculate the average as a floating point number:

```c
float average = (float) class_size_total / total_classes;
```

Here we **explicitly** cast `class_size_total` to a `float`, then perform the division, which will now result in a floating point value.

The variable `class_size_total` isn't permanently changed to a `float`; rather the value is treated as the float in that statement. `class_size_total` is always an `int` in this program.

To explicitly cast a variable to a different data type, we would write:

```
(new_data_type) variable_name
```

In some cases, the C compiler will **implicitly cast** a variable to a different data type. This happens when assigning a floating point value to an `int`:

```c
float pi = 3.14159;
int a = pi;
```

Since an integer cannot store any values after the decimal point, the floating point value, `pi`, is **implicitly** cast to an `int` as it as assigned to the variable `a`.

**Explicitly** casting is generally preferred from a stylistic perspective, so that others can more easily understand your code.

{% next %}

## More Applications of Typecasting

Recall that the [ASCII standard](https://study.cs50.net/slideshows/1w3Ynz9oAJvVSIKZnloDngCWzlHuyd79tAaFRbOHTLD4/img/1.png) assigns a unique number to each letter to be able to store characters as binary data. For example, `A` maps to 65, `B` to 66, etc. So another use of typecasting is to convert between `int` values and `char` values.

The programs `ascii0.c` and `ascii1.c` demonstrate both explicit and implicit casting of `char`'s to `int`'s. Go ahead and compile these two programs, included on the right, and see how they work.

It's good to note that some data types are more appropriate for casting than others. For instance, command-line arguments are always `string`s. When the program requires this argument to be used as an `int`, it cannot be cast directly from a `string` to an `int`. Rather a function such as `atoi()` must be used to convert the `string` 3 to the `int` 3.

## Your Turn

We can cast a `char` to an `int`, what do you think would happen if we cast `'A'` to an `int`, added 1 and then cast this back to a `char` before printing.

{% spoiler %}

We should see an output of `B`.

{% endspoiler %}

Your job is to edit the program, `typecasting.c` on the right to do exactly that to the string named `plaintext`. Instead of just outputting the string exactly as it's input, add one to each `char` before printing it.

You may implicitly or explicitly cast each `char` in `plaintext` to an `int`, then add 1 and output each resulting `char`.

Try testing your code with strings containing both uppercase and lowercase letters, numbers and symbols. What happens when your string includes the letter `z`?

{% spoiler %}

Notice the mapping between chars and ints in the [ASCII table](https://study.cs50.net/slideshows/1w3Ynz9oAJvVSIKZnloDngCWzlHuyd79tAaFRbOHTLD4/img/1.png). Each character in `plaintext` should be shifted by one.

{% endspoiler %}

[For more info on typecasting, download the CS50 typecasting Sheet](https://ap.cs50.school/assets/pdfs/unit2/typecasting.pdf)
