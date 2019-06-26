# Types

Recall that Python supports multiple "types," among them strings (aka `str`) and integers (aka `int`). Suffice it to say the type of a variable matters!

Consider the program in `types.py` in the text editor at top-right. At first glance, it looks like it

1. prompts the user for two inputs, `x` and `y`,
1. adds `x` and `y`, storing the sum in `z`, and
1. prints z.

But let's look more closely.

Type

```
python types.py
```

in the terminal window at bottom-right, followed by Enter. When prompted for `x`, input `1`, followed by Enter. When prompted for `y`, again input `1`, followed by Enter. You should see the result.

How curious!

{% next %}

Contrary to what this program thinks, 1 plus 1 does not equal 11! The sum should, of course, equal 2.

Modify `types.py` in the text editor at top-right in such a way that the program correctly outputs the sum of `x` and `y`.

{% spoiler "Hint" %}

Recall that you can cast (i.e., convert) a `str` (e.g., `s`) that looks like an `int` to an actual `int` (e.g., `i`) with code like the below.

```
i = int(s)
```

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/types
```
