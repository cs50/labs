# Variables

In this lab you will learn about:

- The difference between variables in Math and CS
- Creating and naming a variable
- Assigning a value to a variable
- Getting user input for a variable

## What is a Variable?
In computer programming, a **variable** is a container that holds numbers, words, or other types of data to use in our program. Variables in programming are similar to the variables we use in math class, since they both represent a value. Unlike variables in math, variables in programming do not represent an "unknown", and hold values that can change as the program executes.

Another difference is in variable names. In math, variables are only one letter long, as in *x*, or *y*, or *n*. In most programming languages, variable names can be a single letter, a word or a phrase (as long as there are no spaces). In fact, it's considered good programming practice, to use variable names that represent the data they are being used to store.

For instance, we might store a name in a variable `name`, and an age in a variable `age`. We can combine multiple words with underscores, such as `student_name`, and `teacher_name`. But if we create a variable name with a space in it, such as `student name`, our program won't understand what we want it to do!

{% next %}

## Declaring a Variable
In the C programming language, we have to create, or declare, a variable before we can use it. We do this by telling the program the type of data our variable will hold, followed by the name of the variable, as in:

```c
int age;
```

This declares the variable `age` as an integer, meaning it can only hold whole numbers.

If we use a variable before declaring it, we'll generate an error when we try to compile our program.

{% next %}

## Assigning a Value to a Variable

To store a number in the variable we just declared we can write:

```c
age = 18;
```
The `=` sign here works differently than it does in your math class. In programming, `=` means assignment, not equality. It says to the computer: `age` gets 18.

Assignment always works from right to left. In other words, the value on the right side of the `=` is evaluated first and then stored in the variable whose name is on the left side of the `=`.

One thing that look strange to most people who start programming for the first time, is an expression like:

```c
age = age + 1;
```

In math class, we know this can never be true! How can age equal itself plus one?

But if we remember that the `=` represents assignment, and not equality, we can read this as: evaluate the result of adding one to the value stored in `age`, then reassign this new value to `age`.

Keep in mind when we write a statement like this, we must have already assigned an initial value to `age`. In other words:

```c
int age;
age = age + 1;
```

will generate an error, because `age` is declared, but not have a value when we try to add one to it.

Instead, we'll assign a starting value to `age` and then increase it by one:

```c
int age;
age = 18;
age = age + 1;
```

A shortcut we can take is to declare and initialize a variable in one line of code like this:

```c
int age = 18;
```

{% next %}


## Getting User Input

So we've seen how we can code values into a variable by typing them into our program, but what if we want a use a different value for a variable each time we run it?

In this case we can use CS50's user input functions, to prompt for a value in the terminal.

![Prompting](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/variables/variables2.gif)

There are several CS50 user input functions, depending on the type of data (data type) that we want our variable to hold. Since `age` is an int, we could user `get_int()` to prompt for a value like this:

```c
age = get_int("Enter Your Age: ");
```

The function `get_int()` takes an argument, which is the text that we want to prompt the user with. Note that the prompt is wrapped inside of double quotes, `"` since it is a string, the argument is inside of parentheses `(` and `)` and the line ends with `;`.

Do note that `age` would have had to be declared earlier on in our program for this code to execute.

We could, of course, declare `age` and get user input in one line of code:

```c
int age = get_int("Enter Your Age: ");
```

To use the CS50 user input functions, we do have to include the CS50 library by typing in:

```
#include <cs50.h>
```

at the top of our program.

{% next %}

## Now It's Your Turn!

Though the program on the right is correct and will execute properly, it is not well designed. For one thing, what if we want to start with different ages each time we run it? It's a lot of work to have to change each occurrence of `17` to whatever age the user wants to use!

(As well soon see, the code also contains **magic numbers** which will soon learn about in a future lab!)

So your job is to edit the code provided, to use one or more variables, along with user input.

To start, declare a new variable `age` as an int and use `get_int()` with get a value from the user.

Now replace every occurrence of `17` with `age`, so that the program uses the variable rather than the hardcoded number for each calculation.

When you are done, compile your program by typing the following in the terminal window after the `$` prompt followed by enter:

```
make variables
```

If you see any errors, it's time to debug! You may have left out something small like a `;` or misspelled something. If you have a hard time finding your error, try "prepending" `help50` to your command like this:

```
help50 make variables
```

Once you feel you've corrected any errors, execute `make variables` again, and repeat this process until no more errors appear.

Then execute your program, by typing in the following, again followed with enter:

```
./variables
```

Hopefully you should now see the prompt you've written. Enter a number and see what happens!

{% next %}

## Testing

### Correctness

Practice testing your own code by trying out different kinds of inputs. We want to get into the habit of testing our code not only valid inputs, but for invalid inputs, as well as "corner cases", which would be inputs that aren't technically invalid, but are not what you might normally expect to see as an input.

What happens if you enter name instead of your age, when you get the prompt, as in:

```
Enter Your Age: Brian
Enter Your Age:
```

Does the program come back and ask again? It should do this because `get_int()` only accepts integers.

Or if you enter a number with a decimal point:

```
Enter Your Age: 17.5
Enter Your Age:
```

The program again should come back and repropmt.

What if you enter a negative number? At the prompt, try entering:

```
Enter Your Age: -15
```

You might see your program do the calculation correctly, but how can one be `-15` years old?

Eventually we will see how to validate user inputs, but for now, our goal is to practice using variables, and to write code that is syntactically correct, which will compile and execute.

### Style

Since we want to get into good habits early, check that your indentation, and spacing is correct, by typing:

```
style50 variables.c
```

[For more info on variables, download the CS50 Variables Reference Sheet](https://ap.cs50.school/assets/pdfs/unit1/variables.pdf)

