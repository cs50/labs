# Exit Codes

In this lab you will learn:

- What is meant an by exit code
- How do we use exit codes

## What is an Exit Code?

You may have noticed that the `main()` function has a return type of `int`, yet we haven't been returning anything at the end of the main function.

It turns out that the compiler automatically adds a `return 0` in our main function, if we don't specify anything. This value is called an **exit code**. As our programs get longer and more complex, these exit codes will become a valuable tool.

## Using Exit Codes

By convention, when a program executes successfully, it should return an exit code of 0. That's why the compiler assumes that if no return statement is provided at the end of main, the program should return 0. We can add `return 0` anywhere we want in our program as well. As soon as the program executes a return statement, it will immediately terminate, even if it's not at the end of the program.

{% next %}

We can see what value our program returns by typing in `echo $?` at the terminal prompt immediately after executing our program.

If a value other than 0 is returned from main, this generally means that some type of error was encountered while executing our program. This could be that an input validation check failed, or perhaps the program requires two command-line arguments, and the user only input one. We might have our program return a non-zero exit code to signal an error:

```c
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./hello <name>\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}
```

In the program above, we are expecting two command-line arguments. The `if` statement checks to see if the argument count, `argc`, is not equal to 2, in which case it prints an error message and returns 1, stopping the program from executing any further. The line:

```c
printf("hello, %s\n", argv[1]);
```

only executes when the argument count is correct. The final `return 0` is not required here, but is considered good practice.

{% next %}

## Your Turn

Change the program on the right to use exit codes, rather than an if...else statement to stop the program from executing when the argument count is incorrect.

Then compile and test your program, with the correct and incorrect number of command-ine arguments. Try typing in `echo $?` at the `$` after executing your program both ways to further that you've implemented exit codes correctly!

And don't forget to check your style with:

```
style50 exit.c
```

[For more info, download the CS50 Exit Code Sheet](https://ap.cs50.school/assets/pdfs/unit2/exit_codes.pdf)
