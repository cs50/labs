---
foo: bar
results:
  exists:
    description: "caesar.c exists."
    status: true
    log:
      - "checking that caesar.c exists..."
  compiles:
    description: "caesar.c compiles."
    status: true
    log:
      - "running clang caesar.c -o caesar -std=c11 -ggdb -lm -lcs50..."
      - "checking that program exited with status 0..."
  encrypts_a_as_b:
    description: "encrypts \"a\" as \"b\" using 1 as key"
    status: null
    log: []
---

# Loops

If you ever played Super Mario Bros. back in the day, you might recall this scene, wherein four question marks were hovering in the sky:

{% assign foo = "bar" %}

{{ foo }}

{{ results }}

{{ results.exists }}

![bricks](bricks.png)

Let's recreate a bit of that game, albeit in text!

In `mario.py`, implement a program that prints, quite simply, `????`, without using a loop.


{% check "Does your compile?" %}
{% if compiles.passed %}
  Yes! Nicely done!
{% else %}
  {{ compiles }}
{% endif %}
{% endcheck %}

{% check "Does your code print `????`?" %}
{{ nope }}
{% endcheck %}

{% check "Does your code avoid using a loop?" %}
TODO
{% endcheck %}

{% next %}

Elsewhere in Super Mario Bros., there might be more (or even fewer) than four question marks in the sky. Let's prepare for as much.

Modify `mario.py` in the text editor at top-right in such a way that the program prints, quite simply, `????`, this time using a loop to print each question mark one at a time, each on the same line.

{% spoiler Hint %}
To print a question mark without a newline (i.e., carriage return) after it, use

```
print("?", end="")
```

which appends `""` (i.e., the "empty string") to each question mark instead of, `"\n"` (which represents a newline), the default.

Indeed,

```
print("?")
```

is actually equivalent to

```
print("?", end="\n")
```

but is quicker to type!
{% endspoiler %}

{% next %}

Okay, your program still only prints four question marks, and somehow we've gone and made it more complicated nonetheless. But consider that just a step toward this final goal! (Boss level!)

Modify `mario.py` in the text editor at top-right in such a way that the program

1. prompts the user for a positive integer, and
2. prints that many question marks, all on the same line.

{% submit %}
