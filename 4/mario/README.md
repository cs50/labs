# Mario

Toward the end of World 1-1 in Super Mario Bros., Mario must ascend a right-aligned half pyramid of blocks before leaping (if he wants to maximize his score) toward a flag pole:

![right-aligned pyramid](mario_right_shifted.png)

Let's recreate that pyramid with Python, albeit in text, using hashes (`#`) for bricks.

{% next %}

Let's start by building the opposite of that right-aligned half pyramid, a left-aligned half pyramid like this:

```
#
##
###
####
#####
######
#######
########
```

Each hash is a bit taller than it is wide, so not to worry that the half pyramid itself is taller than it is wide!

In `mario.py` in the text editor at top-right, implement a program that

1. prompts the user for an integer between 1 and 8, inclusive, re-prompting the user (again and again as needed) if his or her input is less than 1 or greater than 8,
1. prints a left-aligned half pyramid of that height.

{% spoiler "Hints" %}

If the user inputs `1`, your output should resemble:

```
#
```

If the user inputs `2`, your output should resemble:

```
#
##
```

And if the user inputs `8`, your output should resemble:

```
#
##
###
####
#####
######
#######
########
```

{% endspoiler %}

{% next %}

Let's now right-align that left-aligned half pyramid by pushing its hashes to the right by prefixing them with dots using periods (`.`):

```
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

Modify `mario.py` in the text editor at top-right in such a way that the program prints a right-aligned half pyramid of the prescribed height, prefixing its hashes with dots.

{% spoiler "Hints" %}

If the user inputs `1`, your output should still resemble:

```
#
```

If the user inputs `2`, your output should now resemble:

```
.#
##
```

And if the user inputs `8`, your output should now resemble:

```
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

{% endspoiler %}

{% next %}

Let's now get rid of those dots!

Modify `mario.py` in the text editor at top-right in such a way that the program prints only a half pyramid of the prescribed height, without any dots, replacing the periods with spaces (using your space bar).

{% spoiler "Hints" %}

If the user inputs `1`, your output should still resemble:

```
#
```

If the user inputs 1, your output should now resemble:

```
 #
##
```

And if the user inputs `8`, your output should now resemble:

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
pip3 install --upgrade 'submit50<3' &>/dev/null && submit50 cs50/labs/pdss/4/mario
```
