# Bleep

At right is a program that's supposed to censor messages that contain words that appear on a list of banned words, as in the below.

```
$ python bleep.py banned.txt
What message would you like to censor?
What the heck
What the ***

$ python bleep.py banned.txt
What message would you like to censor?
gosh darn it
**** **** it
```

Unfortunately, the program doesn't actually censor those messages yet! Instead, it just prints out the original message.

Modify `bleep.py` in such a way that the program:

* Opens the file specified in `sys.argv[1]` and reads from that file a list of words, one per line, storing each in some data structure for later access. You might want to consider a `list` or `set`.
* Splits the user's input into individual words, using the [`split`](https://docs.python.org/3/library/stdtypes.html#str.split) method on the `message`.
* Iterates over the words returned by calling `split`, checking to see if any of the words match (case-insensitively) any of the words in the banned list.
* Prints back the message, but with all of the characters in any banned words replaced by a `*` character.
* For example, `gosh` should be replaced with four `*` characters, while `fudge` should be replaced with five.
* You should not censor words that merely contain a banned word as a substring. For example, if **bar** is a banned word in the provided list, then none of **bar**ns nor crow**bar** nor wheel**bar**row should be censored.

{% spoiler "Hints" %}

* You can use the [`len`](https://docs.python.org/3/library/functions.html#len) function to get the number of characters in a string.

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/bleep
```
