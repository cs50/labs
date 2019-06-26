# Conditions

If you ever played Super Mario Bros. back in the day, you might also recall this scene, wherein Mario had to jump over a stack of three bricks:

![three bricks in a column](mario.png)

Elsewhere in the game, Mario had to jump over more (or fewer) bricks. Of course, it'd be unreasonable to have him jump over more than 4 bricks. (He's not Yoshi!)

Let's recreate that aspect of the game, albeit in text, using hashes (`#`) for bricks!

In `mario.py` in the text editor at top-right, implement a program that

1. prompts the user for an integer between 1 and 4, inclusive, re-prompting the user (again and again as needed) if their input is less than 1 or greater than 4,
1. prints precisely that many hashes, one per line, followed by a newline.

{% spoiler "Hints" %}

Recall that you can induce an "infinite loop" with code like:

```
while True:
```

And recall that you can break out of an (otherwise) infinite loop with code like:

```
while True:
    if something is True:
        break
```

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/conditions
```
