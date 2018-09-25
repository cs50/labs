# Whodunit

{% video https://www.youtube.com/watch?v=NkUf9vj1iFA %}

{% next %}

## The Shadow Knows

Welcome to Tudor Mansion. Your host, Mr. John Boddy, has met an untimely end—he’s the victim of foul play. It is your job to determine whodunit.

Unfortunately for you (though even more unfortunately for Mr. Boddy), the only evidence you have is a 24-bit BMP file called `clue.bmp`, pictured below, that Mr. Boddy whipped up on his computer in his final moments (what a guy!). Hidden among this file’s red "noise" is a drawing of whodunit.

![the final clue](clue.bmp)

{% next %}

## Safecracker

Your task is to design and implement a program, `crack`, that cracks passwords. We're not going to give too many hints on this one, but to get started you may want to read up on how the `crypt` function works on Unix/Linux systems, such as this lab environment. To do so, type:

```
man crypt
```

in the terminal. Take particular note of that program's mention of "salt". Per that "`man` page", you'll likely want to put

```
#define _XOPEN_SOURCE
#include <unistd.h>
```

at the top of your file in order to use `crypt`. Use `pseudocode.txt` as a notepad for ideas as to how you should organize your program!

### Specification

* Your program should accept one and only one command-line argument: a hashed password.
* If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error (of your choice) and exit immediately, with `main` returning `1` (thereby signifying an error).
* Otherwise, your program must proceed to crack the given password, ideally as quickly as possible, ultimately printing the password in the clear followed by `\n`, nothing more, nothing less, with `main` returning `0`.
* Assume that each password has been hashed with C's DES-based (not MD5-based) `crypt` function.
* Assume that each password is no longer than five (5) characters. Gasp!
* Assume that each password is composed entirely of alphabetical characters (uppercase and/or lowercase).

Below, then, is some example behavior.

```
$ ./crack
Usage: ./crack hash
```

```
$ ./crack 50cI2vYkF0YU2
LOL
```

{% spoiler "Hints" %}

* Recall that `argc` and `argv` give us information about what was typed at the command line.
* Recall that a string is just an array of characters (`char`s).
* Recall that we can access individual elements of an array using square brackets (`[ ]`).
* Recall that the salt is the first two characters of the hash.
* Recall that sometimes, people use passwords that are actual words. Perhaps there's an optimization that can be employed?
* Brute force algorithms aren't the fastest, and that's okay! Recall that shorter passwords are usually easier to crack than longer ones.

{% endspoiler %}

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/2018/fall/crack
```
