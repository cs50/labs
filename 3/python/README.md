# Python

Recall that Python is a programming language with which you can write programs on your own Mac or PC. All you need is a text editor (in which to write the program) and a terminal window (in which to run the program).

In Week 3's videos, for instance, David used a text editor called Atom with a built-in terminal window, inside of which he had installed Python. But no need to install either! Instead, this here lab has both built-in for you: at top-right is a code editor, and at bottom-right is a terminal window.

In fact, let's take them out for a spin and write (perhaps) your very first program in Python, one that simply says hello to the world.

{% next %}

Notice how the code editor at top-right already has a file called `hello.py` open for you. Recall that `.py` is, by convention, the "file extension" that indicates that a file contains Python code.

Go ahead and type precisely the below into `hello.py` in the text editor at top-right:

```
print("hello, world")
```

No need to save the file; it'll be automatically saved for you.

{% next %}

Let's now run your program. 

Type precisely the below into the terminal window at bottom-right, to the right of the dollar sign (`$`), otherwise known as a prompt, followed by Enter:

```
python3 hello.py
```

You should see `hello, world`, followed by another prompt? If so, nicely done! If not, simply review these instructions and try again!

{% next %}

To submit your work, type precisely the below into the terminal window at bottom-right, followed by Enter. Put another way, "execute" the below.

```
submit50 cs50/labs/pdss/3/python
```

If prompted, input your GitHub username and password; for security, you'll see asterisks (`*`) instead of your actual password.
