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
* Splits the user's input into individual words, ...

TODO

{% spoiler "Hints" %}

TODO

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/bleep
```
