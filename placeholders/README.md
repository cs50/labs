# Printf Placeholders

In this lab you will learn:

- Why we use placeholders
- How to use a placeholder to format a variable for `printf`
- Different placeholders for different data types
- Using multiple placeholders in one statement

## What is a Placeholder?

One way of using `printf` is to simply type some text, surrounded by double quotes, inside of parentheses as in:

```c
printf("hello, world\n");
```

The `\n` is a special character that represents "new line". When this line of code is executed inside of a program, it will output:

```
hello, world
```

But what if we want to print a number, or something other than a pre-defined string? That's where strange looking syntax (`%i`, `%s`, etc.) comes in!

These symbols are **placeholders** for data stored in a variable. They are also referred to as **format strings** since they format the value that a variable holds, to be printed inside of a string.

{% next %}

## Using Placeholders with `printf`

The placeholder is used to hold the place for the value that you want to print. For example:

```c
printf("hello, %s\n", name);
```

means to take the value of the string variable, `name`, and substitute this value for the placeholder, `%s`. Notice that the double quote includes the `\n` since this is the new line character which is printed, and that a comma (`,`) follows the close quote, which is then followed by the variable to print.

So if the value stored in the variable `name` is "Zamyla", this line of code would output:

```
hello, Zamyla
```

Another thing to keep in mind is that `printf` does not automatically put line breaks at the end of a line, which is why you'll want to put `\n` as the last character inside the string that `printf` takes to tell your program to print a line break.

{% next %}

## Different Placeholders for Different Data Types

Different data types use different format strings. Here is a list for reference.

| Data Type     | Placeholder       | Example |
| ------------- |------------------| ------- |
| int           | %i               | printf("Age: %i\n", age);|
| long long     | %lli             | printf("My ID number is %lli\n", id_number);|
| float, double | %f               | printf("The value of pi is %f\n", pi); |
| string        | %s               | printf("hello, %s\n", name);|
| char          | %c               | printf("Enter Y or N: %c\n", agreement);|

## Specifying How Many Decimal Places

Note that `%f` is the placeholder for both floats and doubles. It automatically defaults to printing exactly six places after the decimal point. You can have it print more or fewer places after the decimal, with a bit of extra syntax.

To print out one place after the decimal point we use `%.1f`, two places after the decimal, `%.2f`, 55 places after the decimal `%.55f`, etc.

{% next %}

## More than One Variable in One Statement

We can print more than one variable in a `printf` statement, by using multiple placeholders in the output string, and multiple variables, separated by commas. For instance:

```c
printf("My name is %s and my age is %i.\n", name, age);
```

The value of `name` is substituted for the first placeholder, which is `%s` and age is substituted for the second placeholder, `%i`. We can print more variables in this statement as well by using additional placeholders and additional variables. The number of placeholders and the number of variables must be the same.

{% next %}

## Now it's Your Turn!

The program on the right has several variables of different types declared, with CS50 user input functions getting user input. Write a `printf` statement, using these variables, to print out a statement that looks something like:

```
The <animal> jumped over the <body>, <number> times.
```

Where `<animal>` is replaced by the value of the variable `animal` that you input, `<body>` is replaced with the value of `body`, and `<number>` is replaced by the value of `number`.

Note that the data type for `number` is a float. What does that tell us?

To make things interesting, print out the value of `number` with exactly one value after the decimal point.

So if you input *cow* for `animal`, *moon* for `body` and *2.5* for `number`, your sentence should print:

```
The cow jumped over the moon, 2.5 times.
```
{% next %}

## Testing

Try entering different inputs for the three variables. What happens if you enter a number for the variable `animal`? Do you get strange results? Since `get_string()` accepts a `string`, which is a series of characters, it will accept numbers, letters, or even punctuation as part of the `string`. Down the road we'll practice checking for valid text input, but for now, let's just make sure our program runs.

You can check your style by typing:

```
style50 placeholders.c
```

It's good to get into good habits now, so when you start writing longer and more complex programs, you will know how to style your code properly. Code that is properly styled, is much easier to debug!
