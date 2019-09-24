# Arrays and Strings

In this lab you will learn:

- What is an array
- How we create and use arrays
- Why a `for` loop is so useful for arrays and strings

## What is an Array?

An **array** is a type of data structure in C that can hold multiple values, of the same type, in one variable. There are many reasons we may want to do this. Say, for instance, we want to get the average grade for a class of 30 students. We can create 30 variables, get user input for each of these, add them up and divide by 30:

```c
float student1 = get_float("Enter a grade for student1: ");
float student2 = get_float("Enter a grade for student2: ");
float student3 = get_float("Enter a grade for student3: ");
...
```

We can see pretty quickly that it's going to get pretty boring typing in so much repetitive code!

Instead, we can use an array, named `student` that can store 30 floating point values:

```c
float student[30];
```

{% next %}

We access individual values in `student` by using square bracket notation with an index that ranges from 0 up to, but not including 30. Arrays in C are **zero-indexed**, meaning the first item in the array always has an index of zero.

Once our array is declared, we can prompt for grades like this:

```c
student[0] = get_float("Enter a grade for student0: ");
student[1] = get_float("Enter a grade for student1: ");
student[2] = get_float("Enter a grade for student2: ");
...
```

or even better, we can prompt 30 times for input using a loop:

```c
for (int i = 0; i < 30; i++)
{
    student[i] = get_float("Enter a grade for student %i", i);
}
```

Note that we use the variable `i` both to control the `for`  loop, as well as to the index into our array. Since `i` starts at 0 and increases by one until it gets to 29, it corresponds to each index in our array. This is called iterating through an array.

{% next %}

## Strings

Arrays in C can store values of any data type, as long as all elements in the array are of the same type. In fact, a **string** in C is really an array of `chars`.

When we declare a string in C as in:

```c
string course = "CS50";
```

we are creating an array named `course` with one character at each index. There is one additional character at the end of every string in C: the null-terminator, represented by `'\0'`. The null-terminator is the character that tells a string that the string is over, and that there are no more characters in the string. So this array will have five spots for chars, indexed 0 through 4.

We can index into this string in the same way we index into any array, using square bracket notation. So `course[0]` has a value of `'C'`, `course[1]` a value of `'S'`, ending with `course[4]` having a value of `'\0'`. Even though `'\0'` looks like two characters, our program see it as one `char`.

Since a string is an array, we can iterate through a string using a for loop as well. There is a special function `strlen()` we can use which gives us the length of a string. To use this function, we need to write `#include <string.h>` at the top of our program to access the `string.h` library.

Our for loop to access each character of our string, one `char` at a time would look like:

```c
for (int i = 0; i < strlen(course); i++)
{
    printf("%c\n", course[i]);
}
```

Here we print out each letter stored in the string variable `course` on its own line.

{% next %}

## Your Turn!

To the right are two programs you will complete. First, you'll modify `string.c` to include a for loop that iterates through the string `name` and print out one character per line.

Then complete the program `array.c` which creates a new integer array named `hours`, in which you will input the number of hours you spent on homework each day for the last 5 days, and then print out the hours for each day. Your output should look like:

```
Day 1: <day 1 hours>
Day 2: <day 2 hours>
```

and so on, where `<day 1 hours>` is replaced with the number you input for day 1.

{% spoiler "Hint" %}
You can use a for loop like this to prompt for the number of hours for each of the 5 days:

```c
for (int i = 0; i < NUM_DAYS; i++)
{
    // prompt for hours using `get_int()` and store the result in `hours[i]`
}
```

Then use the same for loop a second time to iterate through these values and print them. Inside this second loop you will have something like:

```c
printf("Day %i: %i", i + 1, hours[i]);
```

Why do you think we're printing the value `i + 1` for the day?

{% endspoiler %}

Make sure to compile and test both programs!

[Download our CS50 Reference sheet on Arrays and Strings](https://ap.cs50.school/assets/pdfs/unit2/arrays_and_strings.pdf)
