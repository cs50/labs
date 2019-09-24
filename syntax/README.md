# Syntax

![SyntaxVideo](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/syntax/syntax.gif)

In this lab you will learn:

- What syntax is
- When to use parentheses and double quotes
- Why we use curly braces and semicolons
- The syntax needed to create a program in C

## What is Syntax?

In linguistics, syntax is the set of rules for using words, phrases and punctuation to form sentences. As you can see above, if the word order of a sentence is incorrect, you might not understand what is being said to you.

{% next %}

## Syntax in C

In Computer Science, **syntax** is also important for a computer to understand what you are telling it to do. Each programming language has its own syntactical rules, which include the combination of both words and punctuation.

For instance, to say "hello" in C, we would write:

```c
printf("hello,  world\n");
```

The `printf` function in C, is the equivalent to the `say` block in Scratch. Note that our `printf` function takes an **argument**, or parameter, which is wrapped in symmetrical parentheses, `(` and `)`.

You may also notice the double quotes `"`, which are also symmetrical, and which surround words, or sequences of characters. We'll start calling these sequences of characters `strings`.

And finally, the entire line ends with a semicolon, `;`. A semicolon is used at the end of every statement, like a period at the end of a sentence.

{% next %}

## Creating a Program

Just like how we need the `when green flag` clicked block in Scratch to start our program, our C program won’t run unless we write a few lines to set it up.

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

Notice the `int main(void)` line, which is the standard name in C of a default function which is required for the program to run. When you execute a C program, the `main` function will automatically run.

Don't worry yet about the terms `int` and `void`! We'll be learning more about those later on.

The curly braces `{` and `}` are symbols you'll see frequently in C. They are used here to wrap the code that we want to execute in functions like `main`. You'll soon see curly braces used with loops, to indicate which segments of code to repeat; with conditional statements to tell the computer which block to to run for each of the conditions if they are true, and with other programing constructs as well.

The line `#include <stdio.h>` may not be obvious at first. The term `include` is a keyword that indicates we want to include some other file in our program, and it must be preceded by the symbol `#`. The **library**,`stdio.h`, contains (and we only know from searching online and looking at [documentation](https://man.cs50.io/). the standard input/output library, which means that it deals with input (like from the keyboard) and output (printing characters to the screen). In fact, it contains the code of `printf()` that we are using. There is no equivalent in Scratch, since by default the functions are already defined and created for us.

{% next %}

## Now it's Your Turn!

Now it's your turn to try out decoding some syntax in C!

Take a look at the program on the right. There are several syntactical errors in it. See if you can edit the code to correct the errors. Look carefully at all the details in the example above for reference.

When you are done, **compile** your program by typing the following in the terminal window after the `$` prompt followed by Enter.

```
make syntax
```

If you see any errors, it's time to debug! You may have left out something small like a `;` or misspelled something. If you have a hard time finding your error, try "prepending" `help50` to your command like this:

```
help50 make syntax
```

Once you feel you've corrected any errors, execute `make syntax` again, and repeat this process until no more errors appear.

Then execute your program, by typing in the following, again followed with `enter`:

```
./syntax
```

<style type="text/css">
#green {color:green;}  
</style>

### Styling with `style50`

Though C doesn't care about how you style your code (in other words code with correct syntax but inconsistent spacing will compile and execute), CS50 does! That's because spacing your code consistently makes it easier to read and as we'll see soon, easier to debug.

You can check that your spacing is correct by executing the following at the `$` prompt:

```
style50 syntax.c
```

If there’s room for improvement in your code’s style, highlighted in red will be any characters you should delete, and highlighted in green will be any characters you should add.

When style50 outputs:

<div id="green">
    <pre><code>Looks good!</code></pre>
</div>

you are done! Congratulations, you've completed the Syntax Lab!

[For more info, download the CS50 Syntax Reference Sheet](https://ap.cs50.school/assets/pdfs/unit1/syntax.pdf)
