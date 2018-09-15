# Mario

{% video https://www.youtube.com/watch?v=C-5-22ZvW40 %}

## Background

Toward the end of World 1-1 in Nintendo's Super Mario Brothers, Mario must ascend right-aligned pyramid of blocks, a la the below.

![screenshot of Mario jumping up a right-aligned pyramid](pyramid.png)

Let's recreate that pyramid in C, albeit in text, using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramid itself is also be taller than it is wide.

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

The program we'll write will be called `mario`. And let's allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between, say, 1 and 8, inclusive. 

Here's how the program might work if the user inputs `8`:

```
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Here's how the program might work if the user inputs `4`:

```
$ ./mario
Height: 4
   #
  ##
 ###
####
```

Here's how the program might work if the user inputs `2`:

```
$ ./mario
Height: 2
 #
##
```

And here's how the program might work if the user inputs `1`:

```
$ ./mario
Height: 1
#
```

If the user doesn't, in fact, input a positive integer between 1 and 8, inclusive, the program should re-prompt the user until they cooperate:

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```

How to begin? Let's approach this problem one step at a time.

{% next %}

## Pseudocode

First, write in `pseudocode.txt` at right some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There's no one right way to write pseudocode, but short English sentences suffice. Recall how we wrote pseudocode for [finding Mike Smith](https://cdn.cs50.net/2018/fall/lectures/0/lecture0.pdf). Odds are your pseudocode will use (or imply using!) one or more functions, conditions, Boolean expressions, loops, and/or variables.

{% spoiler %}

There's more than one way to do this, so here's just one!

<ol>
  <li>Prompt user for height</li>
  <li>If height is less than 1 or greater than 8 (or not an integer at all), go back one step</li>
  <li>
    Iterate from 1 through height:
    <ol>
      <li>On iteration <em>i</em>, print <em>i</em> hashes and then a newline</li>
    </ol>
  </li>
</ol>

It's okay to edit your own after seeing this pseudocode here, but don't simply copy/paste ours into your own!

{% endspoiler %}

## Building the Opposite

It turns out it's a bit easier to build a left-aligned pyramid Let's start by building the opposite of that right-aligned pyramid, a left-aligned pyramid like this:

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

