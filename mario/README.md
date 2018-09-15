# Mario

{% video https://www.youtube.com/watch?v=C-5-22ZvW40 %}

{% next %}

## World 1-1

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

Here's how the program might work if the user inputs `8` when prompted:

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

Here's how the program might work if the user inputs `4` when prompted:

```
$ ./mario
Height: 4
   #
  ##
 ###
####
```

Here's how the program might work if the user inputs `2` when prompted:

```
$ ./mario
Height: 2
 #
##
```

And here's how the program might work if the user inputs `1` when prompted:

```
$ ./mario
Height: 1
#
```

If the user doesn't, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

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

<p>
  There's more than one way to do this, so here's just one!
</p>

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

<p>
  It's okay to edit your own after seeing this pseudocode here, but don't simply copy/paste ours into your own!
</p>

{% endspoiler %}

{% next %}

## Prompting for Input

Whatever your pseudocode, let's first write only the C code that prompts (and re-prompts, as needed) the user for input. 

Specifically, modify `mario.c` at right in such a way that it prompts the user for the pyramid's height, storing their input in a variable, re-prompting the user again and again as needed if their input is not a positive integer between 1 and 8, inclusive. Then, simply print the value of that variable, thereby confirming (for yourself) that you've indeed stored the user's input successfully, a la the below.

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
Stored: 4
```

{% spoiler "Hints" %}

<ul>
  <li>Recall that you can compile your program with <code>make</code>.</li>
  <li>Recall that you can print an <code>int</code> with <code>printf</code> using <code>%i</code>.</li>
  <li>Recall that you can get an integer from the user with <code>get_int</code>.</li>
  <li>Recall that <code>get_int</code> is declared in <code>cs50.h</code>.</li>
  <li>Recall that we prompted the user for a positive integer in class via <a href="https://sandbox.cs50.io/b56865fd-c861-425f-aad7-4adcf6831139"><code>positive.c</code>.</li>
</ul>

{% endspoiler %}

## Building the Opposite

Now that your program is (hopefully!) accepting input as prescribed, it's time for another step.

It turns out it's a bit easier to build a left-aligned pyramid than right-, a la the below.

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

So let's build a left-aligned pyramid first and then, once that's working, right-align it instead!

Modify `mario.c` at right such that it no longer simply prints the user's input but instead prints a left-aligned pyramid of that height.

{% spoiler "Hints" %}

<ul>
  <li>Keep in mind that a hash is just a character like any other, so you can print it with `printf`.</li>
  <li>Just as Scratch has a <a href="https://cdn.cs50.net/2018/fall/lectures/0/lecture0.pdf">Repeat</a> block, so does C have a <a href="https://cdn.cs50.net/2018/fall/lectures/1/lecture1.pdf"><code>for</code></a> loop, via which you can iterate some number times. Perhaps on each iteration, <em>i</em>, you could print that many hashes?</li>
  <li>
    You can actually "nest" loops, iterating with one variable (e.g., <code>i</code>) in the "outer" loop and another (e.g., <code>j</code>) in the "inner" loop. For instance, here's how you might print a square of height and width <code>n</code>, below. Of course, it's not a square that you want to print!
<pre>
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n; j++)
    {
        printf("#");
    }
    printf("\n");
}
</pre>
  </li>
</ul>

{% endspoiler %}

